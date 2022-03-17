from django.db import models

# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    pridmet = models.CharField(max_length=250)
    message = models.TextField(default=0)

    def __str__(self):
        return self.name