from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:category>/<str:article_name>/', views.article_view, name='article_view'),
]