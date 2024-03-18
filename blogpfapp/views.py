from django.shortcuts import render, get_object_or_404, redirect
from .models import blog

from .forms import BlogForm

def delete_blog(request, blog_id):
    blog_instance = get_object_or_404(blog, id=blog_id)

    if request.method == 'POST':
        blog_instance.delete()
        return redirect('blog_list')  # Redirect to the blog list or another page

    return render(request, 'delete_blog.html', {'blog_instance': blog_instance})

def blog_list(request):
    blog_posts = blog.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def web2db(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BlogForm()

    return render(request, 'web2db.html', {'form': form})

def frontpage(request):
    post = blog.objects.all()
    return render(request, "frontpage.html", {"blogdata": post})

def edit_blog(request, blog_id):
    blog_instance = get_object_or_404(blog, id=blog_id)

    if request.method == 'POST':
        # If the form is submitted, process the data
        form = BlogForm(request.POST, request.FILES,instance=blog_instance)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirect to the blog list or another page after editing
    else:
        # If it's a GET request, initialize the form with existing data
        form = BlogForm(instance=blog_instance)

    return render(request, 'edit_blog.html', {'form': form, 'blog_instance': blog_instance})
