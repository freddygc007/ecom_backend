from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    LIVE=1
    DELETED=0
    DELETE_CHOICES = ((LIVE,"Live"),(DELETED,"Delete"))
    name = models.CharField(max_length=255)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")
    phone = models.CharField(max_length=255)
    deleted_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    