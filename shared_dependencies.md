1. **Shared Variables:**
   - `main_image_url`: This variable is used to store the URL of the main product image. It is defined in the `product_template.py` model and used in the `product_template_view.xml` and `product_image.js` files.
   - `extra_media_urls`: This variable is used to store the URLs of additional product media. It is defined in the `product_template.py` model and used in the `product_template_view.xml` and `product_image.js` files.

2. **Data Schemas:**
   - `product.template`: This is the main data schema that is extended in the `product_template.py` file. The new fields `main_image_url` and `extra_media_urls` are added to this schema.

3. **DOM Element IDs:**
   - `main_image`: This is the ID of the DOM element where the main product image is displayed. It is used in the `product_image.js` and `product_image.xml` files.
   - `extra_media`: This is the ID of the DOM element where the additional product media are displayed. It is used in the `product_image.js` and `product_image.xml` files.

4. **Function Names:**
   - `display_main_image`: This function is defined in the `product_image.js` file to display the main product image from the `main_image_url`.
   - `display_extra_media`: This function is defined in the `product_image.js` file to parse and display each URL from the `extra_media_urls` as a separate image.

5. **Message Names:**
   - `Invalid_URL_Error`: This message is used in the `product_template.py` file to indicate an error when the URL validation fails.
   - `Loading_Error`: This message is used in the `product_image.js` file to indicate an error when there is a problem loading the images from the URLs.

6. **CSS Class Names:**
   - `product-main-image`: This class is defined in the `product_image.css` file and used in the `product_image.xml` file to style the main product image.
   - `product-extra-media`: This class is defined in the `product_image.css` file and used in the `product_image.xml` file to style the additional product media.

7. **Test Names:**
   - `test_main_image_url`: This test is defined in the `test_product_image.py` file to test the functionality related to the `main_image_url`.
   - `test_extra_media_urls`: This test is defined in the `test_product_image.py` file to test the functionality related to the `extra_media_urls`.

8. **Module Name:**
   - `product_image`: This is the name of the module that is defined in the `manifest.py` and `README.md` files. It is also used as the prefix for the file paths in the `manifest.py` file.