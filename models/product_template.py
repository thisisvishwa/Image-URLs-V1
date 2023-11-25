```python
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    main_image_url = fields.Char(string='Main Image URL')
    extra_media_urls = fields.Text(string='Extra Media URLs')

    def validate_url(self, url):
        # Add URL validation logic here
        # Raise an error if the URL is not valid
        # Message: Invalid_URL_Error
        pass
```