from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):  
    model = ProductImage
    extra = 1 
    fields = ('image', 'alt_text')  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'get_categories', 'price', 'rating',)
    filter_horizontal = ('categories',)
    ordering = ('sku',)
    inlines = [ProductImageInline]  

    def get_categories(self, obj):
        return ", ".join([category.friendly_name or category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)