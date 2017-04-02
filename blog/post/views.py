from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from user_profile.models import User
from .models import Post, Category

class Profile(View):
    def get(self, request,username):
        params = {}
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user)
        params['posts'] = posts
        params['author'] = user

        return render(request, 'profile.html', params)

class UsersPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all()
        users = User.objects.all()
        categories = Category.objects.all()
        params['posts'] = posts
        params['users'] = users
        params['categories'] = categories
        return render(request, 'index.html', params)

# class AllCateg(View):
#     def get(self, request):
#         params = {}
#         categories = Category.objects.all()
#         params['categories'] = categories
#         return render(request, 'index.html', params)

class Detail(View):
    def get(self,request, Category_id):
        return HttpResponse('<h1>the details of the categorey'+Category_id+'</h1>')






