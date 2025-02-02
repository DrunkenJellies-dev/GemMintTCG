from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'get_categories', 'price', 'rating', 'image',)
    filter_horizontal = ('categories',)
    ordering = ('sku',)

    def get_categories(self, obj):
        return ", ".join([category.friendly_name or category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)