from pytest import fixture
from playwright_stealth import Stealth
from dotenv import load_dotenv
from os import getenv

load_dotenv()

stealth = Stealth()

@fixture
def stealth_page(context):
    page = context.new_page()
    stealth.apply_stealth_sync(page)
    yield page
    page.close()

@fixture
def invalid_user_creds():
    return {
        'email': getenv('INVALID_EMAIL'),
        'password': getenv('INVALID_PASS')
    }

@fixture
def valid_user_creds():
    return {
        'email': getenv('VALID_EMAIL'),
        'password': getenv('VALID_PASS')
    }
