from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(("blog_image"), upload_to='blog_image/')
    post = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    

