from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog
from .forms import Blog_form
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def blog_list(request): #list
    blog_list = Blog.objects.all().order_by('-发布时间')
    #搜索的实现
    query = request.GET.get('q')
    if query:
        blog_list = blog_list.filter(
            Q(标题__icontains=query)|
            Q(内容__icontains=query)
              )
    context = {
        'blog': blog_list
    }
    return render(request, 'list.html', context)

def blog_detail(request, id): #detail
    instance = get_object_or_404(Blog,id=id)
    context = {
        'instance': instance
    }
    return render(request, 'detail.html', context)

def blog_create(request): #create
    form = Blog_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'successfully created')
        return HttpResponseRedirect("/blog/%s" % instance.id)
    context = {
        "form": form,
    }
    return render(request, 'form.html', context)

def blog_update(request, id): #update
    #instance = Blog.objects.get(id=id)
    instance = get_object_or_404(Blog, id=id)
    form = Blog_form(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'saved')
        return redirect("/blog/%s" % instance.id)
    context = {
        "form": form,
    }
    return render(request, 'form.html', context)

def blog_delete(request, id): #delete
    instance = get_object_or_404(Blog, id=id)
    instance.delete()
    messages.success(request,"deleted")
    return redirect("index")