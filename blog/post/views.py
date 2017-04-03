from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views import View
from user_profile.models import User
from .models import Post, Category



class Index(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        users = User.objects.all()
        categories = Category.objects.all()
        params['posts'] = posts
        params['users'] = users
        params['categories'] = categories
        return render(request, 'index.html', params)


class AllPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        params['posts'] = posts
        return render(request, 'posts.html', params)


class Blog(View):
    def get(self, request, blogname):
        content = {}
        blog = User.objects.get(blog_name=blogname)
        posts = blog.post_set.all().order_by('-release_date')
        content['blog'] = blog
        content['posts'] = posts
        return render(request, 'user_blog.html',content)


# class Blog_content(View):
#     def get(self, request, username):
#         params = {}
#         user = User.objects.get(username=username)
#         posts = Post.objects.filter(author=user).order_by('-release_date')
#         params['posts'] = posts
#         params['author'] = user
#         return render(request,'user_blog.html', params)



class Blog_content(View):
    def get(self, request,username):
        author = get_list_or_404(User, username=username)
        return render(request, 'user_blog.html', {'author': author})


class Detail(View):
    def get(self,request, Category_id):
        category = get_object_or_404(Category, id=Category_id)
        return render(request, 'categ_detail.html', {'category': category})






