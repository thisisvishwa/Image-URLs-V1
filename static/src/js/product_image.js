odoo.define('product_image', function (require) {
    'use strict';

    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    publicWidget.registry.ProductImage = publicWidget.Widget.extend({
        selector: '.oe_product',
        events: {
            'load': '_onLoad',
        },

        start: function () {
            var self = this;
            this.display_main_image();
            this.display_extra_media();
            return this._super.apply(this, arguments);
        },

        display_main_image: function () {
            var main_image_url = this.$el.data('main-image-url');
            if (main_image_url) {
                var img = $('<img/>', { 
                    id: 'main_image',
                    src: main_image_url, 
                    alt: 'Main Product Image'
                });
                this.$el.append(img);
            } else {
                console.error('Loading_Error: Main image URL is not provided.');
            }
        },

        display_extra_media: function () {
            var extra_media_urls = this.$el.data('extra-media-urls');
            if (extra_media_urls) {
                var urls = extra_media_urls.split(',');
                for (var i = 0; i < urls.length; i++) {
                    var img = $('<img/>', { 
                        id: 'extra_media_' + i,
                        src: urls[i], 
                        alt: 'Extra Product Media ' + (i + 1)
                    });
                    this.$el.append(img);
                }
            } else {
                console.error('Loading_Error: Extra media URLs are not provided.');
            }
        },

        _onLoad: function () {
            this.$el.removeClass('oe_product_loading');
        },
    });

    return publicWidget.registry.ProductImage;
});