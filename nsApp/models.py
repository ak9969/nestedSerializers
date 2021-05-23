from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=1,decimal_places=1)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
