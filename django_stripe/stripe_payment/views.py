import os

import stripe

from django.views import View
from django.views.generic import DetailView, TemplateView
from django.http import JsonResponse

from .models import Item


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class ItemDetailView(DetailView):
    template_name = 'base.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": os.getenv('STRIPE_PUBLIC_KEY'),
        })
        return context


class ProductLandingPageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            "STRIPE_PUBLIC_KEY": 'pk_test_51LiNQfIVxJYT0CqkZ2oaZqAlJtCEqv0Q6U575wvZTLdqzc2ncpAMDk1BXSiyzygaN3JuHGcQgfXp5UN8lPWC7ByN00U5fZAw9d',
        })
        return context


class CreateCheckoutSessionView(View):

    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success.html',
            cancel_url='http://127.0.0.1:8000/cancel.html',
        )
        return JsonResponse({
            'id': session.id
        })

    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success.html',
            cancel_url='http://127.0.0.1:8000/cancel.html',
        )
        return JsonResponse({
            'id': session.id
        })
