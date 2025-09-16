from django.shortcuts import render
from . models import Student

# Create your views here.
def create(request):
    if request.POST:
        title=request.POST.get('title')
        su=request.POST.get('summary')
        ye=request.POST.get('year')
        obj=Student(title=title,summary=su,year=ye)
        obj.save()

    return render(request,'create.html')
def list(request):
    return render(request,'list.html')
def edit(request):
    return render(request,'edit.html')