from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , UserManager
from django.contrib.auth.hashers import make_password

class UserDetails(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField(null=True)
    password = models.CharField(max_length=255)
    joined_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

    # def save(self, *args, **kwargs):
    #     if not self.pk:  # If the object is being created
    #         self.password = make_password(self.password)  # Hash the password before saving
    #     super().save(*args, **kwargs)
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255,null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=True,null=False)
    description = models.TextField(null=True,default=False)
    
    def __str__(self):
        return self.name
    
@property
def imageURL(self):
	try:
		url = self.image.url
	except:
		url = ''
	return url

    
class Orders(models.Model):
    customer = models.ForeignKey(UserDetails, on_delete=models.SET_NULL ,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItems(models.Model):
    product = models.ForeignKey(Products,blank=True,on_delete=models.SET_NULL ,null=True)
    order = models.ForeignKey(Orders,blank=True,on_delete=models.SET_NULL ,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    


