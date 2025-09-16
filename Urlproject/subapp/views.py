from django.shortcuts import render
from . models import Student
from . forms import StudentForm

# Create your views here.
def create(request):
    frm=StudentForm()
    if request.POST:
        title=request.POST.get('title')
        su=request.POST.get('summary')
        ye=request.POST.get('year')
        obj=Student(title=title,summary=su,year=ye)
        obj.save()

    return render(request,'create.html',{'frm':frm})



def list(request):
    database_value=Student.objects.all()
    return render(request,'list.html',{'fullvalue':database_value})

def table(request):
    database_value=Student.objects.all()
    return render(request,'table.html',{'database_value':database_value})
def edit(request,pk):
    print(pk)
    get_id=Student.objects.get(pk=pk)
    print(get_id)
    if request.POST:
        get_id.title=request.POST.get('title')
        get_id.summary=request.POST.get('summary')
        get_id.year=request.POST.get('year')
        get_id.save()
    return render(request,'edit.html',{'e':get_id})

def delete(request,pk):
    get_id=Student.objects.get(pk=pk)
    get_id.delete()
    database_value=Student.objects.all()
    return render(request,'table.html',{'database_value':database_value})

    database_value=Student.objects.all()
    return render(request,'table.html',{'database_value':database_value})