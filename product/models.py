from django.db import models

from django.utils.text import slugify




# Create your models here.

class CategoryManager(models.Manager):
    def True_status(self):
        return self.filter(status=True)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    status = models.BooleanField(default=True)
    objects = CategoryManager()

    def __str__(self):
        return self.title
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Category, self).save()

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
    category = models.ManyToManyField(Category, blank=True, null=True, related_name='products')
    body = models.TextField()
    image = models.ImageField(upload_to='images/products')
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    color = models.ManyToManyField(Color, blank=True, null=True, related_name='products')
    size = models.ManyToManyField(Size, related_name='products')

    def __str__(self):
        return self.title



class Information(models.Model):
    product = models.ForeignKey(Product,null=True ,on_delete=models.CASCADE, related_name='informations')
    text = models.TextField()

    def __str__(self):
        return self.text[:30]



