import posts
from django.urls import path

#from . import views
from .views import PostList, PostDetail


urlpatterns = [
    #path('', views.posts_list, name="home"),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]
