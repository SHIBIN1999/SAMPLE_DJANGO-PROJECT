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
    database_value=Student.objects.all()
    return render(request,'list.html',{'fullvalue':database_value})

def table(request):
    database_value=Student.objects.all()
    return render(request,'table.html',{'database_value':database_value})
def edit(request):
    return render(request,'edit.html')