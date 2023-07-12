from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='Items', on_delete=models.Case)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=255, default="Unknown")
    image = models.ImageField(upload_to='Item-Images', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='Items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url