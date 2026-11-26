from django.test import TestCase

from .models import Product


class ProductViewTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Wireless Mouse',
            description='Ergonomic wireless mouse.',
            price='24.99',
        )

    def test_home_displays_products(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, '$24.99')

    def test_product_detail_displays_product(self):
        response = self.client.get(f'/products/{self.product.pk}/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)
        self.assertContains(response, '$24.99')
