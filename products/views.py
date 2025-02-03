from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from products.forms import ProductForm
from .models import Product, Category, ProductImage
from django.urls import path
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower

# Create your views here.

def all_products(request):
    """ A view to show all products including sorting and search queries"""

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'categories':
                sortkey = 'categories__name' 
                products = products.prefetch_related('categories')

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Filtering by categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(categories__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Searching by query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')  

        if form.is_valid():
            product = form.save()
            for file in files:
                ProductImage.objects.create(product=product, image=file)  
            messages.success(request, "Product added successfully!")
            return redirect('products')  

    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        files = request.FILES.getlist('images')  # Get new images

        if form.is_valid():
            product = form.save()
            for file in files:
                ProductImage.objects.create(product=product, image=file)  # Save new images
            messages.success(request, "Product updated successfully!")
            return redirect('edit_product', product_id=product.id)

    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
