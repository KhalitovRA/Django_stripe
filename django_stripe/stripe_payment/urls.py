from django.urls import path

from . import views

urlpatterns = [
    path('item/<int:pk>/', views.ItemDetailView.as_view()),
    path('buy/<int:pk>/', views.CreateCheckoutSessionView.as_view(), name='buy'),
    path('', views.ProductLandingPageView.as_view(), name='landing-page'),
]
