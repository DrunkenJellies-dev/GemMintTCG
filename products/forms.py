from django import forms
from .models import Product, Category, ProductImage

class ProductForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,  
        required=False
    )

    class Meta:
        model = Product
        fields = ['name', 'sku', 'description', 'has_condition', 'price', 'rating', 'image_url', 'categories']

    def save(self, commit=True):
        product = super().save(commit=False)  
        if commit:
            product.save()
            self.save_m2m()  
        return product
