from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(default = None, max_length = 300)
    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING,
    blank= True, null = True)
    name = models.CharField(default = None, max_length = 300)
    price = models.IntegerField(default = None, blank = True, null = True)
    imgsrc = models.ImageField(upload_to="static/images/products", default = None, blank = True)
    def __str__(self):
        return self.name


def delall():
    c =  Category.objects.all()
    p = Product.objects.all()
    p.delete()
    c.delete()
    print('deleted all')