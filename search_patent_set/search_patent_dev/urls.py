from . import views

from django.urls import path

urlpatterns = [
    path('', views.list, name='home'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('filter/', views.filter, name='filter'),

]