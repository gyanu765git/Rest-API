from django.db import models

# Create your models here.


class apiModel(models.Model):
    name=models.CharField(max_length=20, null=True,blank=True)
    des = models.TextField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name\
