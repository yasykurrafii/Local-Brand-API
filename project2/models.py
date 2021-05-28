from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    website = models.CharField(max_length=100, null=True, default='-')
    tokped = models.CharField(max_length=100, null=True, default='-')
    shopee = models.CharField(max_length=100, null=True, default='-')
    ig = models.CharField(max_length=100, null=True, default='-')

    class Meta:
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.brand_name

class Type(models.Model):
    type_pakaian = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipe Pakaian'

    def __str__(self):
        return self.type_pakaian

class Image(models.Model):
    image_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image_product/')

    def __str__(self):
        return self.image_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    type_pakaian = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ManyToManyField(Image)
    brand = models.ManyToManyField(Brand)
    price = models.IntegerField(default='0')
    deskripsi = models.TextField(null=True)

    class Meta:
        verbose_name = 'Product'
    
    def __str__(self):
        return self.product_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
