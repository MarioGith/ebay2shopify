"""Module providing test."""
import pytest
from src.ebayapi.ebay_data import EbayData
from src.ebayapi.exceptions import (
    TokenNotDefined,
    AppIdNotDefined,
    CertIdNotDefined,
    DevIdNotDefined,
)


def test_token_not_defined(mock_env_token_missing):
    # pylint: disable=unused-argument
    """Test TOKEN not defined"""
    with pytest.raises(TokenNotDefined):
        _ = EbayData()


def test_app_id_not_defined(mock_env_app_id_missing):
    # pylint: disable=unused-argument
    """Test APP_ID not defined"""
    with pytest.raises(AppIdNotDefined):
        _ = EbayData()


def test_cert_id_not_defined(mock_env_cert_id_missing):
    # pylint: disable=unused-argument
    """Test CERT_ID not defined"""
    with pytest.raises(CertIdNotDefined):
        _ = EbayData()


def test_dev_id_not_defined(mock_env_dev_id_missing):
    # pylint: disable=unused-argument
    """Test DEV_ID not defined"""
    with pytest.raises(DevIdNotDefined):
        _ = EbayData()
