from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from products.sitemaps import ProductSitemap, StaticViewSitemap
from . import views

sitemaps = {
    "products": ProductSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]