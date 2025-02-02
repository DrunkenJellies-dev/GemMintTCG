from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    condition = None
    if 'product_condition' in request.POST:
        condition = request.POST['product_condition']
    bag = request.session.get('bag', {})

    if condition:
        if item_id in list(bag.keys()):
            if condition in bag[item_id]['items_by_condition'].keys():
                bag[item_id]['items_by_condition'][condition] += quantity
            else:
                bag[item_id]['items_by_condition'][condition] = quantity
        else:
            bag[item_id] = {'items_by_condition': {condition: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    condition = None
    if 'product_condition' in request.POST:
        condition = request.POST['product_condition']
    bag = request.session.get('bag', {})

    if condition:
        if quantity > 0:
            bag[item_id]['items_by_condition'][condition] = quantity
            messages.success(request,
                             (f'Updated condition {condition.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_condition"][condition]}'))
        else:
            del bag[item_id]['items_by_condition'][condition]
            if not bag[item_id]['items_by_condition']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed condition {condition.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        condition = None
        if 'product_condition' in request.POST:
            condition = request.POST['product_condition']
        bag = request.session.get('bag', {})

        if condition:
            del bag[item_id]['items_by_condition'][condition]
            if not bag[item_id]['items_by_condition']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed condition {condition.upper()} '
                              f'{product.name} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
