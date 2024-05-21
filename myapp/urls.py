from django.urls import path
from .views import *

urlpatterns = [
    path('home/', maqola, name='maqola'),
    path('world/', world_news , name='world' ),
    path('local/' , local_news , name='local' ),
    path('sport/', sports_news , name='sport' ),
     path('article_detail/<int:id>/', article_detail, name='article_detail'),
]