import stripe
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect, render



stripe.api_key = settings.STRIPE_PRIVATE_KEY

def buy_item(request, id):
    session = stripe.checkout.Session.create(
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': 'T-shirt',
            },
            'unit_amount': 2000,
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel'
    )

    return JsonResponse({'id':session.id}) #вернул "id": "cs_test_a1YBWLSRm5TN0GmrGnShVQYja5cjiwUaP1cJRWlI1ygKx7rpn5AlRLDJ1h"



def item_detail(request, id):
    context = {
        'id': id,
        'public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'payment/buy_item.html', context)

from django.shortcuts import render

# Create your views here.
