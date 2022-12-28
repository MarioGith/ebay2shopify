"""Module providing test."""
import os
import pytest


def pytest_configure():
    """Create configuration for tests"""
    # Names of variables in env and in app object
    pytest.APP_ID_ENV_NAME = "APP_ID"
    pytest.CERT_ID_ENV_NAME = "CERT_ID"
    pytest.DEV_ID_ENV_NAME = "DEV_ID"
    pytest.TOKEN_ENV_NAME = "TOKEN"
    pytest.API_KEY_ENV_NAME = "API_KEY"
    pytest.SECRET_ENV_NAME = "SECRET"
    pytest.SHOP_URL_ENV_NAME = "SHOP_URL"
    pytest.SHOPIFY_TOKEN_ENV_NAME = "SHOPIFY_TOKEN"

    # Make ENV more accessible
    pytest.APP_ID = os.environ[pytest.APP_ID_ENV_NAME]
    pytest.CERT_ID = os.environ[pytest.CERT_ID_ENV_NAME]
    pytest.DEV_ID = os.environ[pytest.DEV_ID_ENV_NAME]
    pytest.TOKEN = os.environ[pytest.TOKEN_ENV_NAME]
    pytest.API_KEY = os.environ[pytest.API_KEY_ENV_NAME]
    pytest.SECRET = os.environ[pytest.SECRET_ENV_NAME]
    pytest.SHOP_URL = os.environ[pytest.SHOP_URL_ENV_NAME]
    pytest.SHOPIFY_TOKEN = os.environ[pytest.SHOPIFY_TOKEN_ENV_NAME]


@pytest.fixture
def mock_env_token_missing(monkeypatch):
    """This fixture deletes the TOKEN from env"""
    monkeypatch.delenv(pytest.TOKEN_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_app_id_missing(monkeypatch):
    """This fixture deletes the APP_ID from env"""
    monkeypatch.delenv(pytest.APP_ID_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_cert_id_missing(monkeypatch):
    """This fixture deletes the CERT_ID from env"""
    monkeypatch.delenv(pytest.CERT_ID_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_dev_id_missing(monkeypatch):
    """This fixture deletes the DEV_ID from env"""
    monkeypatch.delenv(pytest.DEV_ID_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_api_key_missing(monkeypatch):
    """This fixture deletes the API_KEY from env"""
    monkeypatch.delenv(pytest.API_KEY_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_secret_missing(monkeypatch):
    """This fixture deletes the SECRET from env"""
    monkeypatch.delenv(pytest.SECRET_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_shop_url_missing(monkeypatch):
    """This fixture deletes the SHOP_URL from env"""
    monkeypatch.delenv(pytest.SHOP_URL_ENV_NAME, raising=False)


@pytest.fixture
def mock_env_shopify_token_missing(monkeypatch):
    """This fixture deletes the SHOPIFY_TOKEN from env"""
    monkeypatch.delenv(pytest.SHOPIFY_TOKEN_ENV_NAME, raising=False)
