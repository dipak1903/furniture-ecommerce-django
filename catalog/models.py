from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Chair', 'Chair'),
        ('Table', 'Table'),
        ('Cupboard', 'Cupboard'),
        ('Bench', 'Bench'),
        ('Bed', 'Bed'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='product_images/')  

    def __str__(self):
        return self.name
