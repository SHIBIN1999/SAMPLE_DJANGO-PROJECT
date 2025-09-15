from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def create(request):
    s={'title':'the drak','summary':'very good story','year':1999,'success':False}
    return render(request,'create.html',s)