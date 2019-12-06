
from rest_framework import serializers
from .models import Director, Movie, Actor, User, Comment
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('NameDir', 'idDir')
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','slug','title','gender','language','year','contentRating','duration','cover','description','source','identifier')
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    def update(self,instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.title = validated_data.get('title', instance.title)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.language = validated_data.get('language', instance.language)
        instance.year = validated_data.get('year', instance.year)
        instance.contentRating = validated_data.get('contentRating', instance.contentRating)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.description = validated_data.get('description', instance.description)
        instance.source = validated_data.get('source', instance.source)
        instance.identifier = validated_data.get('identifier', instance.identifier)
        instance.save()
        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('NameAc','idAc','AcMov')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Name','Email','Password','IDUser')
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('idComment','idMovie','text','userName')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idComment = validated_data.get('idComment', instance.idComment)
        instance.idMovie = validated_data.get('idMovie', instance.idMovie)
        instance.text = validated_data.get('text',instance.comment)
        instance.userName = validated_data.get('userName',instance.userName)
        instance.save()
        return instance

