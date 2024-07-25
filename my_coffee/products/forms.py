from django import forms # Form
from .models import Product # Model Product


class ProductForm (forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')  # View Client
    description = forms.CharField(max_length=300, label='Descripción')
    price = forms.DecimalField(
        max_digits=10, decimal_places=2, label='Precio'
    )  # 10 numbres / 2 decimals
    available = forms.BooleanField(initial=True, label='Disponible', required=False)
    photo = forms.ImageField(label='Foto', required=False)

    #Method Submit
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'], # Clean Info from customer request 
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
        )