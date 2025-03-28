from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', maqola, name='maqola'),
    path('home/', world_news , name='world' ),
    path('fotos/' , local_news , name='local' ),
    path('', sports_news , name='sport' ),
     path('article_detail/<int:id>/', article_detail, name='article_detail'),
]