"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from post.views import UsersPosts,Detail,AllPosts
from user_profile.views import Profile
from post import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/(\w+)/$', Profile.as_view(), name="profile_detail"),
    url(r'^$',UsersPosts.as_view()),
    url(r'^posts/(?P<Category_id>[0-9]+)/$', Detail.as_view(),name="detail"),
    url(r'^posts/$', AllPosts.as_view()),



]
