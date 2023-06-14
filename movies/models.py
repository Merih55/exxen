from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="Film İsmi")
    image = models.ImageField(upload_to='movies/', verbose_name="Film Resmi")
    # pip install Pillow kodunu yazmayı unutma(ImageField kullanmak için)

    def __str__(self):
        return self.name