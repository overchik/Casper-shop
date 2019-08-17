from django.db import models

class Goods(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(("image"), upload_to='image/')
    taste = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    stock = models.BooleanField()
    
    
    def __str__(self):
        return self.title
