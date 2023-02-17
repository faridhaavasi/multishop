from django.db import models

# Create your models here.

class Color(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    CHOISES = (
        ('el', 'electronic'),
        ('cl', 'clothing'),

    )
    type = models.CharField(max_length=2, choices=CHOISES)
    title = models.CharField(max_length=20)
    body = models.TextField()
    image = models.ImageField(upload_to='images/products')
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    color = models.ManyToManyField(Color, related_name='product', blank=True, null=True)
    size = models.ManyToManyField(Size, related_name='product', blank=True, null=True)

    def __str__(self):
        return self.title






