from app.models import Category_choices, Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "slug", "category", "product_image","marked_price",
                  "selling_price", "description", "brand"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            
            "product_image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "marked_price": forms.NumberInput(attrs={
                "class": "form-control",
                "required":False,
                "placeholder": "Marked price of the product..."
            }),
            "selling_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Selling price of the product..."
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description of the product...",
                "rows": 5
            }),
            "brand": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product brand here..."
            })
        }


        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category_choices
        fields = ["title", "slug"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique product here..."
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
        }


    
        

