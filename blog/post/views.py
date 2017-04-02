from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from user_profile.models import User
from .models import Post, Category



class UsersPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        users = User.objects.all()
        categories = Category.objects.all()
        params['posts'] = posts
        sort_params = []

        params['users'] = users
        params['categories'] = categories
        return render(request, 'index.html', params)


class AllPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        params['posts'] = posts
        return render(request, 'posts.html', params)


class AllPostsD(View):
    def get(self, request):
        # posts = get_object_or_404(Post, id=int(post_date)).order_by('-release_date')
        posts = Post.objects.all().order_by('-release_date')
        return render(request, 'posts.html', {'posts': posts})

class Detail(View):
    def get(self,request, Category_id):
        category = get_object_or_404(Category, id=Category_id)
        return render(request, 'categ_detail.html', {'category': category})






