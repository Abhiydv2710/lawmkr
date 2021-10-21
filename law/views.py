from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from law.models import Category,bookmark






# Create your views here.

def home(request):
    cats = Category.objects.all()

    data  = {
        'cats': cats
    }

    return render(request, 'home.html', data)


def category(request,url):
    Category
    return render(request,"category.html",{})


def searchbar(request):
    cats = Category.objects.all()
    data  = {
        'cats': cats
    }
    if request.method == 'GET':
        search =request.GET.get('search')
        post =Category.objects.all().filter(title=search)
        return render(request,'searchbar.html',{'post':post,'cats':data})

def bookmark(request):
    url=request.GET.get('url')
    print(url)
    return HttpResponse("Bookmark Added")

    