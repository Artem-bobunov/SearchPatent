from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from itertools import groupby
import torch
from .models import Patents,acd_Patents

BLOG_POSTS_PER_PAGE = 3


# from transformers import T5ForConditionalGeneration, T5Tokenizer
# model_name = "0x7194633/keyt5-large" # or 0x7194633/keyt5-base
# tokenizer = T5Tokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)

# device = "cuda" if torch.cuda.is_available() else "cpu"
# model.to(device)
# tokenizer.to(device)
def list(request):
    all_obj = Patents.objects.all()
    paginator = Paginator(all_obj, BLOG_POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request,'list.html',{'pages':pages})


def filter(request):
    list_object = None
    list = None
    pages = None

    print('good')

    query_dict = request.GET
    query = query_dict.get("q")

    if query is not None:
        list_object = Patents.objects.filter(Q(asd__abstract__icontains = query)

                                           ).order_by('-id')
        print('Good')

        paginator = Paginator(list_object, BLOG_POSTS_PER_PAGE)
        page_number = request.GET.get('page')
        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

    return render(request, 'list.html', context={'pages':pages})


# def generate(text, **kwargs):
#     inputs = tokenizer(text, return_tensors='pt')
#     with torch.no_grad():
#         hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
#     s = tokenizer.decode(hypotheses[0], skip_special_tokens=True)
#     s = s.replace('; ', ';').replace(' ;', ';').lower().split(';')[:-1]
#     s = [el for el, _ in groupby(s)]
#     return s



def detail(request,id):
    obj = Patents.objects.get(id=id)
    # abs = generate(obj.asd.abstract,top_p=1.0, max_length=64)
    abs = None
    #cls = generate(obj.asd.claims,top_p=1.0, max_length=64)
    #des = generate(obj.asd.description,top_p=1.0, max_length=64) ,'abs':set(abs)
    return render(request,'detail.html',{'obj':obj,'abs':set(abs)})