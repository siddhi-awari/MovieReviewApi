from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.content[:20]}"

