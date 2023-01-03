from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase, ProductToPurchaseLink

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['person', 'address']

    def form_valid(self, form):
        self.object = form.save()  # создаем запись о заказе
        for product in self.request.POST['products'].split(","):  # проходимся по списку с айди продуктов
            # создаем запись в "many to many" таблице
            ProductToPurchaseLink.objects.create(product=Product.objects.get(pk=product), purchase=self.object)
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')
