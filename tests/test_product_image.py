```python
from odoo.tests import common

class TestProductImage(common.TransactionCase):

    def setUp(self):
        super(TestProductImage, self).setUp()
        self.ProductTemplate = self.env['product.template']
        self.product = self.ProductTemplate.create({
            'name': 'Test Product',
            'main_image_url': 'http://example.com/main.jpg',
            'extra_media_urls': 'http://example.com/extra1.jpg,http://example.com/extra2.jpg'
        })

    def test_main_image_url(self):
        self.assertEqual(self.product.main_image_url, 'http://example.com/main.jpg', 'Main Image URL not correctly set')

    def test_extra_media_urls(self):
        self.assertEqual(self.product.extra_media_urls, 'http://example.com/extra1.jpg,http://example.com/extra2.jpg', 'Extra Media URLs not correctly set')
```