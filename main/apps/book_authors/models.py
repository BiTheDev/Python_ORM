from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors = models.ManyToManyField(Author, related_name="books")

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name="authors")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class books_authors(models.Model):
#     author = models.ForeignKey(Author,related_name="author")
#     book = models.ForeignKey(Book, related_name="book") 
# Author.books.values()
# Book.authors.values()