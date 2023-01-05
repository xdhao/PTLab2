from django.test import TestCase
from shop.models import Product, Purchase, ProductToPurchaseLink
from datetime import datetime


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="beer", price="50")
        Product.objects.create(name="wine", price="350")

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="beer").name, str)
        self.assertIsInstance(Product.objects.get(name="beer").price, int)
        self.assertIsInstance(Product.objects.get(name="wine").name, str)
        self.assertIsInstance(Product.objects.get(name="wine").price, int)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="beer").price == 50)
        self.assertTrue(Product.objects.get(name="wine").price == 350)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_whiskey = Product.objects.create(name="whiskey", price="740")
        self.datetime = datetime.now()
        self.purchase = Purchase.objects.create(person="Ivanov",
                                                address="Svetlaya St.")

        ProductToPurchaseLink.objects.create(product=self.product_whiskey, purchase=self.purchase)

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(pk=self.purchase.pk).person, str)
        self.assertIsInstance(Purchase.objects.get(pk=self.purchase.pk).address, str)
        self.assertIsInstance(Purchase.objects.get(pk=self.purchase.pk).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(pk=self.purchase.pk).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(pk=self.purchase.pk).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(pk=self.purchase.pk).date.replace(microsecond=0) == \
                        self.datetime.replace(microsecond=0))
