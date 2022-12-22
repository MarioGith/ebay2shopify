"""Module providing test."""
import pytest
from src.ebay.ebay_data import EbayData


def test_items_ids_exception():
    """Test exception throwing"""
    ebay_data = EbayData()
    with pytest.raises(ValueError):
        ebay_data.get_items_ids("A string")
