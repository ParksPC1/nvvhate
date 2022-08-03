from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

#for people that post. It ethir published or not
STATUS=((0,"Draft"),(1, "Publish"))




#making tabes for website
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author= models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


# Create your models here.