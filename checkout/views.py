from django.contrib import messages
from django.shortcuts import render, redirect, reverse


# Create your views here.
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GwAMXHTAoCBcf2ymYxl3YLq4QePvZxEQWcPzyt6Ei3ZyYSa0XXRfm3W16T7q5ZH3SR81ptvMuy4G0Pyt4LfF8Dc00PcEOy9D9',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)