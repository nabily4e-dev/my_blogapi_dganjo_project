from django.shortcuts import render

# Create your views here.
from rest_framework import generics
#from rest_framework.generics import ListAPIView

from .models import Post

from .permissions import IsAuthorOrReadOnly

from .serializers import PostSerializer


# class PostListsView(ListAPIView):

#     model = Post

#     queryset = Post.objects.all()

#     template_name = 'posts_list.html'

# def posts_list(request):

#     num_lists = Post.objects.all().count()

#     return render(request, 'posts.html', num_lists)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer