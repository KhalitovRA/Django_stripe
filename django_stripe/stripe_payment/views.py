from django.conf import settings
from django.views.generic import DetailView, TemplateView
from django.http import JsonResponse

from .models import Item
from .forms import ItemForm

from django.views import View
import stripe

from .service import create_checkout_session

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemDetailView(DetailView):
    template_name = 'base.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class ItemView(View):
#
#     def post(self, request):
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             create_checkout_session(stripe=stripe)


class ProductLandingPageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="car")
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": item,
            "STRIPE_PUBLIC_KEY": 'pk_test_51LiNQfIVxJYT0CqkZ2oaZqAlJtCEqv0Q6U575wvZTLdqzc2ncpAMDk1BXSiyzygaN3JuHGcQgfXp5UN8lPWC7ByN00U5fZAw9d'
        })
        return context


class CreateCheckoutSessionView(View):

    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        print(item)
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
        print(item)
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
