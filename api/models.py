from django.db import models


# Create your models here.

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default=0)

    def __str__(self):
        return self.text


class Post(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField(default=0)
    image = models.ImageField(upload_to='posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
