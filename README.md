# Odoo Custom Module for External Product Images

## Introduction

This is a custom Odoo module designed to integrate external URLs for product images. The module allows the storage and display of external image URLs for both the main product image and additional product media within the Odoo eCommerce platform.

## Installation

1. Download the module from the repository.
2. Place the module in your Odoo addons folder.
3. Update the module list in your Odoo instance.
4. Install the module from the apps menu.

## Usage

After installation, you will find two new fields in the product template form view: `main_image_url` and `extra_media_urls`. 

- `main_image_url`: This field is used to store the URL of the main product image.
- `extra_media_urls`: This field is used to store the URLs of additional product media. The field supports multiple URLs, either as a comma-separated string or a JSON structure.

The module will display the images from these URLs in the product view.

## Development Environment

- Odoo Version: 17 CE
- Development Language: Python, XML (for Odoo views)

## Testing

The module should be thoroughly tested in a staging environment before deployment. Test cases are provided in the `tests/test_product_image.py` file.

## Future Considerations

- Potential integration with CDN services for better image delivery.
- Enhanced media handling capabilities (e.g., videos, 3D models).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)