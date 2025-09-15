from django.shortcuts import render

# Create your views here.
def create(request):
    s={'distionary_key':[{'img':'1.jpeg'},
                         {'img':'1.jpeg'},
                         {'img':'1.jpeg'},]}
    return render(request,'create.html',s)
def list(request):
    return render(request,'list.html')
def edit(request):
    return render(request,'edit.html')