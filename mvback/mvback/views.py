    # todo/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets          # add this
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ActorSerializer, UserSerializer, CommentSerializer    # add this
from .models import Director,Movie ,Actor, User, Comment,Rating              # add this
from rest_framework.views import APIView
from rest_framework import status
import hashlib
from rest_framework import mixins, viewsets
from .serializers import LoginSerializer
from .serializers import RatingSerializer




class DirectorView(viewsets.ModelViewSet):# add this
    serializer_class = DirectorSerializer          # add this
    queryset = Director.objects.all()              # add this

class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    def put(self,request,pk):
        saved_movie = get_object_or_404(Movie.object.all(),pk=pk)
        data = request.data.get('Movie')
        serializer = MovieSerializer(instance=saved_movie,data= data, partial= True)
        if serializer.is_valid(raise_exception=True):
            movie_saved = serializer.save()
        return Response({"success:" "Movie '{}' updated successfully".format(movie_saved.title)})
class ActorView(viewsets.ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    def put(self,request,pk):
        saved_comment = get_object_or_404(Comment.object.all(),pk=pk)
        data = request.data.get('Comment')
        serializer = CommentSerializer(instance=saved_comment,data= data, partial= True)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({"success:" "Comment '{}' updated successfully".format(comment_saved.title)})

class Login(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RatingView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()



        
    
