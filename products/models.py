from django.db import models
import random
import os

def upload_path(instance,filename):
    file_new=random.randint(1,2318721983703274)
    name,ext=filepath(filename)
    new_file_name='{file_new}{ext}'.format(file_new=file_new,ext=ext)
    return 'products/{file_new}/{new_file_name}'.format(new_file_name=new_file_name,file_new=file_new)

def filepath(filename):
    file_base=os.path.basename(filename)
    name,ext=os.path.splitext(file_base)
    return name,ext

class ProductManager(models.Manager):

    def get_by_id(self,id):
        qs=self.get_queryset().filter(pk=id)
        if qs.count()==1:
            return qs.first()
        return None


# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,verbose_name=u"Product Name",help_text=u"enter product name")
    slug=models.SlugField(blank=True,unique=True)
    product_description=models.TextField()
    product_price=models.DecimalField(decimal_places=2,default=40.00,max_digits=19)
    product_image=models.ImageField(upload_to=upload_path,blank=True, null=True)
    objects=ProductManager()
    featured=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name





