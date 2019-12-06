from django.contrib import admin
from .models import User,Movie,Director,Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','slug','title','gender','language','year','contentRating','duration','cover','description','source')
class UserAdmin(admin.ModelAdmin):
    list_display =('Name','Email','Password','IDUser')
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('NameDir','idDir')
class ActorAdmin(admin.ModelAdmin):
    list_display = ('NameAc','idAc','AcMov')

admin.site.register(Movie, MovieAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Director,DirectorAdmin)
admin.site.register(Actor,ActorAdmin)
