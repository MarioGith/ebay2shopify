"""Module docstring"""


class ApiKeyNotDefined(Exception):
    """Raise exception if API_KEY doesn't exist"""


class SecretNotDefined(Exception):
    """Raise exception if SECRET doesn't exist"""


class ShopUrlNotDefined(Exception):
    """Raise exception if SHOP_URL doesn't exist"""


class TokenNotDefined(Exception):
    """Raise exception if SHOPIFY_TOKEN doesn't exist"""
