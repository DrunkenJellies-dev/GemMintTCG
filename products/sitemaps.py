from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product

class ProductSitemap(Sitemap):
    changefreq = "weekly"  
    priority = 0.9  

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["home", "products", "contact", "about"]

    def location(self, item):
        return reverse(item)
