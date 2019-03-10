from django import forms
from .models import Prodcut, Review, ProductType

class ProductForm (forms.ModelForm):
    class Meta:
        model = Prodcut
        fields = '__all__'