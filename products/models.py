from django.db import models

# Create your models here.
# Model for products


class Product(models.Model):
    LIVE = 1
    DELETED = 0
    DELETE_CHOICES = ((LIVE, "Live"), (DELETED, "Delete"))
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="media/products/")
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
