from django.db import models


class Director(models.Model):
    NameDir = models.TextField()
    idDir = models.AutoField(primary_key=True)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.TextField()
    title = models.TextField()
    gender = models.TextField()
    language = models.TextField()
    year = models.IntegerField()
    contentRating = models.TextField()
    duration = models.IntegerField()
    cover = models.TextField()
    description = models.TextField()
    source = models.TextField()
    identifier = models.TextField()
    
    def _str_(self):
        return self.title+" ID: "+self.idMovie


class Actor(models.Model):
    NameAc = models.TextField()
    idAc = models.AutoField(primary_key=True)
    AcMov = models.TextField()


class User(models.Model):
    Name = models.TextField()
    Email = models.EmailField(max_length=254)
    Password = models.TextField()
    IDUser = models.AutoField(primary_key=True)
    
    def _str_(self):
        return self.Name+" "+self.Email
class Comment(models.Model):
    idComment= models.AutoField(primary_key=True)
    idMovie = models.IntegerField()
    text = models.TextField()
    userName= models.TextField()
