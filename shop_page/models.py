from django.db import models

class Goods(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(("image"), upload_to='image/')
    taste = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField()
    stock = models.BooleanField()
    
    
    def __str__(self):
        return self
