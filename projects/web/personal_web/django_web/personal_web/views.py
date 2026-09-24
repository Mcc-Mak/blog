from django.shortcuts import render,redirect
from .models import Model
from .forms import BlogForm

# Create your views here.
def index(request):
    return render(request,"home.html")

def resume(request):
    return render(request,"resume.html")

def blog(request):
    entries = Model.objects.all()
    context = {"entries":entries}
    return render(request,"blog.html",context) #Pass context into HTML template

def gallery(request):
    return render(request,"gallery.html")


# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
def add(request):
    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES)
        print(request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form = BlogForm()
    context = {'form':form}
    #entries = Model.objects.all()
    #context = {"entries":entries}
    print(context)
    return render(request,'blog.html',context)

def delete(request):
    if request.method=='POST':
        for key in request.POST.keys():
            ID = key
        print("#{} record is deleted.".format(ID))
        model= Model(id =int(ID))
        model.delete()
        return redirect('/blog')
    else:
        model = Model()
    entries = Model.objects.all()
    context = {"entries":entries}
    return render(request,'blog.html',context)


