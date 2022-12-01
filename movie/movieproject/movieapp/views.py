from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm
# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={
        'moviess':movies
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    MMovie=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'MMovie':MMovie})
def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie1=movie(name=name,desc=desc,year=year,img=img)
        movie1.save()
    return render(request,'add.html')


def update(request,id):
    Movie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request,'edit.html',{'form':form,'Movie':Movie})

def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')
def addi(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.add()
        return redirect('/')
    return render(request,'add.html')
