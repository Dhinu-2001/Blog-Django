from django.db import models
from django.contrib.auth.models import AbstractUser

#User model
class CustomUser(AbstractUser):
    pass

#Blog post model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
