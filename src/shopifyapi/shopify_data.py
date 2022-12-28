"""Module to get shopify data"""
import os
import shopify

from src.shopifyapi.exceptions import (
    ApiKeyNotDefined,
    SecretNotDefined,
    ShopUrlNotDefined,
    TokenNotDefined,
)


class ShopifyData:
    """Gather Shopify data from"""

    def __init__(self):

        # Raise a custom exception if API_KEY is not defined
        try:
            self.api_key = os.environ["API_KEY"]
        except KeyError as err:
            raise ApiKeyNotDefined from err

        # Raise a custom exception if SECRET is not defined
        try:
            self.secret = os.environ["SECRET"]
        except KeyError as err:
            raise SecretNotDefined from err

        # Raise a custom exception if SHOP_URL is not defined
        try:
            self.shop_url = os.environ["SHOP_URL"]
        except KeyError as err:
            raise ShopUrlNotDefined from err

        # Raise a custom exception if SHOPIFY_TOKEN is not defined
        try:
            self.token = os.environ["SHOPIFY_TOKEN"]
        except KeyError as err:
            raise TokenNotDefined from err

        self.api_version = "2022-10"

        shopify.Session.setup(api_key=self.api_key, secret=self.secret)

        self.session = shopify.Session(self.shop_url, self.api_version, self.token)
        shopify.ShopifyResource.activate_session(self.session)

    def get_all_product(self, options):
        """Retrieve all products from Shopify"""
        all_product = []
        page = shopify.Product.find()
        while page.has_next_page():
            all_product += page
            page = page.next_page()
        all_product_ids = map(lambda product: product.id, all_product)
        if options == "list":
            return list(all_product_ids)
        return all_product_ids

    def get_product_by_id(self, product_id):
        """Get product by id on Shopify"""
        product = shopify.Product.find(product_id)
        return product


if __name__ == "__main__":
    shopify_data = ShopifyData()
    shopify_data.get_product_by_id("7292587868315")
