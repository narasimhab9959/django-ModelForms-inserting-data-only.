from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WPMO=WebpageModelForm()
    t={'WPMO':WPMO}

    if request.method=='POST':
        WPMFD=WebpageModelForm(request.POST)
        if WPMFD.is_valid():
            WPMFD.save()
        return HttpResponse('webpage data inserted')
    return render(request,'insert_webpage.html',t)