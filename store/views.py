from django.views.generic import TemplateView


class Store(TemplateView):
    template_name = 'store/store.html'
    

class Cart(TemplateView):
    template_name = 'store/cart.html'
