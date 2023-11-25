{
    'name': 'product_image',
    'version': '1.0',
    'author': 'Vishwa G',
    'category': 'Product',
    'summary': 'Odoo Custom Module for External Product Images',
    'website': '',
    'description': """
    This module integrates external URLs for product images. 
    It allows the storage and display of external image URLs for both the main product image and additional product media within the Odoo eCommerce platform.
    """,
    'depends': ['base', 'product'],
    'data': [
        'views/product_template_view.xml',
        'static/src/xml/product_image.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': ['static/src/xml/product_image.xml'],
    'external_dependencies': {
        'python': [],
    },
}