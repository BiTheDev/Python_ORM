from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    Uploader = models.ForeignKey(User, related_name="Uploaded_book")
    book_likes = models.ManyToManyField(User, related_name="user_likes")
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    
    
    