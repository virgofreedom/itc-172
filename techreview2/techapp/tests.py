from django.test import TestCase
from .models import Prodcut, Review, ProductType
from .forms import ProductForm
##from datetime import datetime
from django.urls import reverse

# Create your tests here.
# model tests

class ProductTest(TestCase):
    def test_stringOutput(self):
        product=Prodcut(productname='Lenovo')
        self.assertEqual(str(product), product.productname)

    def test_tablename(self):
        self.assertEqual(str(Prodcut._meta.db_table), 'product')

class ProductTypeTest(TestCase):
    def test_stringOutput(self):
        producttype=ProductType(typename='Laptop')
        self.assertEqual(str(producttype), producttype.typename)

    def test_tablename(self):
        self.assertEqual(str(ProductType._meta.db_table), 'producttype')

class ReviewTest(TestCase):
    def test_stringOutput(self):
        producreview=Review(reviewtitle='Lenovo')
        self.assertEqual(str(producreview), producreview.reviewtitle)

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

# test view
class TestIndex(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'techapp/index.html')
"""
class TestGetProduct(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reviews/products')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getProducts'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getProducts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/products.html')
"""
# Form test

class New_Product_Form_Test(TestCase):

    # Valid Form Data
    def test_productForm_is_valid(self):
        form = ProductForm(data={'productname': "Lenovo", 'producttype': "laptop", 'user': "rattananeak", 'productentrydate': "2019-01-21", 'producturl':"https://lenovo.com", 'productdescription':"Laptop" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = ProductForm(data={'productname': "Lenovo", 'producttype': "laptop", 'user': "rattananeak", 'productentrydate': "2019-01-21", 'producturl':"https://lenovo.com", 'productdescription':"Laptop" })
        self.assertFalse(form.is_valid())
