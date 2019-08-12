from django.db import models

class Goods(models.Model):

    title = models.CharField(max_length=100)
    taste = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField()
    stock = models.BooleanField()

    
    def __str__(self):
        return self.title
