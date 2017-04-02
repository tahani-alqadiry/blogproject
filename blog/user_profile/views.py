from django.shortcuts import render
from user_profile.models import User
from post.models import Post, Category
from django.views import View

class Profile(View):
    def get(self, request,username):
        params = {}
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user).order_by('-release_date')
        params['posts'] = posts
        params['author'] = user

        return render(request, 'profile.html', params)