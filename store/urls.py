from django.urls import path
from .views import Store, Cart

urlpatterns = [
    path('', Store.as_view(), name='store'),
    path('cart/', Cart.as_view(), name='cart'),
]