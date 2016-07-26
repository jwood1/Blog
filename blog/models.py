from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 300)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
