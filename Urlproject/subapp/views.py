from django.shortcuts import render
from . models import Student
from . forms import StudentForm

# Create your views here.
def create(request):
    
    if request.POST:
      frm=StudentForm(request.POST)
      if frm.is_valid:
          frm.save()
    else:
        frm=StudentForm()

    return render(request,'create.html',{'frm':frm})



def list(request):
    database_value=Student.objects.all()
    return render(request,'list.html',{'fullvalue':database_value})

def table(request):
    database_value=Student.objects.all()
    return render(request,'table.html',{'database_value':database_value})
def edit(request,pk):
    
    get_id=Student.objects.get(pk=pk)
    if request.POST:

        frm=StudentForm(request.POST,instance=get_id)
        if frm.is_valid():
            get_id.save()
    else:
        frm=StudentForm(instance=get_id)    
    return render(request,'create.html',{'frm':frm})


















def delete(request,pk):
    get_ids=Student.objects.get(pk=pk)
    get_ids.delete()
    database_value=Student.objects.all()
    return render(request,'table.html',{'database_value':database_value})

