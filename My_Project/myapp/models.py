from django.db import models
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

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created
            self.password = make_password(self.password)  # Hash the password before saving
        super().save(*args, **kwargs)
