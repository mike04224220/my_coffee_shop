from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='nombre')  # View Client
    description = models.TextField(max_length=300, verbose_name='descripción')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='precio'
    )  # 10 numbres / 2 decimals
    available = models.BooleanField(default=True, verbose_name='disponible')
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='foto')

    def __str__(self): # See prductName
        return self.name