from django.shortcuts import render
from .models import Maqola
from django.contrib.auth.decorators import login_required



# @login_required(login_url='maqola')  ##logout qilinganda login pagega o'tib ketadi
def maqola(request):
    maqolalar = Maqola.objects.all().order_by('-id')  # select * from maqola  order_by id DESC
    context = {
        'maqolalar': maqolalar
    }
    return  render(
        request = request ,
        template_name = 'maqola.html',
        context = context
    )


def world_news(request):
    w_news = Maqola.objects.filter(tag='home').order_by('-id')
    context = {
        'w_news': w_news
    }
    return render(
        request = request,
        template_name='world.html',
        context = context,
    )


def local_news(request):
    l_news = Maqola.objects.filter(tag='fotos').order_by('-id')
    context = {
        'l_news': l_news
    }
    return render(
        request = request,
        template_name='local.html',
        context = context,
    )


def sports_news(request):
    s_news = Maqola.objects.filter(tag='our_service').order_by('-id')
    context ={
        's_news': s_news
    }
    return render(
        request = request,
        template_name='sport.html',
        context = context
    )

def article_detail(request, id):
     maqola = Maqola.objects.get(id=id)
     context = {
         'maqola': maqola
     }
     return render(
         request=request,
         template_name='article_detail.html',
         context=context
     )