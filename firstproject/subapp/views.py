from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def create(request):
    s={'dictionary_key':[{'title':'the drak','summary':'very good story','year':2000,'success':True},
       {'title':'the dream','summary':'very  story','year':2010,'success':True},
       {'title':'the drak','summary':'very good ','year':2015,'success':True}]}
    return render(request,'create.html',s)