from atexit import register
from email.policy import default
from fnmatch import fnmatchcase
from unicodedata import category
from django.db import models
from tables import Description
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
          return self.name


# Create your models here.
class register_info(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)


class register_data(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.email
       

class product(models.Model):
    name =   models.CharField(max_length=50)
    image =  models.ImageField(upload_to ='upload/product')
    price = models.IntegerField(default=100)
    Description = models.CharField(max_length=255, default="good")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)

    def __str__(self): 
        return self.name 

class order(models.Model):
    product = models.ForeignKey(product,on_delete= models.CASCADE)
    customer= models.ForeignKey(register_data,on_delete=models.CASCADE) 
    quality =models.IntegerField(default=1)
    price= models.IntegerField()
    phone= models.IntegerField(default=1)
    address= models.CharField(max_length=50, default="",blank=True)   
    date=models.DateField(default= datetime.datetime.today)
    status=models.BooleanField(default = False)

    
    