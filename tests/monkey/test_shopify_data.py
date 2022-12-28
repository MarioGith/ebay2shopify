"""Module providing test."""
import pytest
from src.shopifyapi.shopify_data import ShopifyData
from src.shopifyapi.exceptions import (
    TokenNotDefined,
    ApiKeyNotDefined,
    SecretNotDefined,
    ShopUrlNotDefined,
)


def test_shopify_token_not_defined(mock_env_shopify_token_missing):
    # pylint: disable=unused-argument
    """Test TOKEN not defined"""
    with pytest.raises(TokenNotDefined):
        _ = ShopifyData()


def test_api_key_not_defined(mock_env_api_key_missing):
    # pylint: disable=unused-argument
    """Test API_KEY not defined"""
    with pytest.raises(ApiKeyNotDefined):
        _ = ShopifyData()


def test_secret_not_defined(mock_env_secret_missing):
    # pylint: disable=unused-argument
    """Test SECRET not defined"""
    with pytest.raises(SecretNotDefined):
        _ = ShopifyData()


def test_shop_url_not_defined(mock_env_shop_url_missing):
    # pylint: disable=unused-argument
    """Test SHOP_URL not defined"""
    with pytest.raises(ShopUrlNotDefined):
        _ = ShopifyData()
