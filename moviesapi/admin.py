from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin. ModelAdmin):
    list_diaplay = ["title", "description", "release_date"]