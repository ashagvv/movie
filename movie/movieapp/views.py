from django.shortcuts import render, redirect
from . models import movies
from . forms import movie_form
# Create your views here.
def fun(request):
    obj=movies.objects.all()
    context={'movie_list':obj

    }
    return render(request,'index.html',context)
def details(request,movie_id):

    obj=movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':obj})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=movies(name=name,desc=desc,year=year,img=img)
        movie.save()

    return render(request,'add.html')
def update(request,id):
    movie=movies.objects.get(id=id)
    form=movie_form(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

