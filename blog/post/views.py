from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from user_profile.models import User
from .models import Post, Category



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


class AllPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all()
        params['posts'] = posts
        return render(request, 'posts.html', params)


# class AllCateg(View):
#     def get(self, request):
#         params = {}
#         categories = Category.objects.all()
#         params['categories'] = categories
#         return render(request, 'index.html', params)

class Detail(View):
    def get(self,request, Category_id):
        category = get_object_or_404(Category, id=Category_id)
        return render(request, 'categ_detail.html', {'category': category})






