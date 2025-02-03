from django.shortcuts import render, redirect, reverse
from django.conf import settings

from django.contrib import messages
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form':order_form,
        'stripe_public_key': 'pk_test_51QoEJqCa0DZAJIS6xWdKl8Ryb3MUR9nHk4n6mpwPsCDseZaWfqk5aGUzWJLeNIoap3R9j2OD3N2eRX1vQHavunmf00dEEicd08',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)