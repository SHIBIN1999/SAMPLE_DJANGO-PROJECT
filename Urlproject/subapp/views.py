from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('summary'))
    return render(request,'create.html')
def list(request):
    return render(request,'list.html')
def edit(request):
    return render(request,'edit.html')