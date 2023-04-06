from django.db import models

# Create your models here.
class acd_Patents(models.Model):
    abstract = models.TextField('Abstract', null=True, blank=True)
    claims = models.TextField('Claims', null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)

class Patents(models.Model):
    number = models.CharField('Номер патента',max_length=100,null=True,blank=True)
    title = models.CharField('Название патента',max_length=255,null=True,blank=True)
    date = models.DateField('Дата публикации',null=True,blank=True)
    country = models.CharField('Страна',max_length=255,null=True,blank=True)
    authors = models.CharField('Авторы',max_length=255,null=True,blank=True)
    mpk = models.CharField('МПК',max_length=255,null=True,blank=True)
    asd = models.ForeignKey(acd_Patents,on_delete=models.CASCADE,null=True, blank=True)

