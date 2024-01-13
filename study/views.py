from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static


def index(request):
    img_url= static('images/26-january.png')
    return render(request,'study/home.html',{'img_url':img_url})


def books(request):
    return HttpResponse("this is a book")


def notes(request):
    return HttpResponse("this is a notes")


def previous_year_paper(request):
    return HttpResponse("this is a previous_year_paper")



