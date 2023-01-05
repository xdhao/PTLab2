from django.test import TestCase, Client
from shop.views import PurchaseCreate
from shop.models import Product, Purchase, ProductToPurchaseLink


class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Product.objects.create(name="beer", price="50")
        Product.objects.create(name="wine", price="350")

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_buy_webpage(self):
        response = self.client.get('/buy/?product_id=7&product_id=8')
        self.assertEqual(response.status_code, 200)

    def test_buy_function(self):
        response = self.client.post('/buy/?product_id=7&product_id=8', {'products': '7,8', 'person': 'Ivanov',
                                                                        'address': 'Svetlaya St.'})
        self.assertEqual(response.status_code, 200)
