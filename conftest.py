from pytest import fixture
from playwright_stealth import Stealth

stealth = Stealth()

@fixture
def stealth_page(context):
    page = context.new_page()
    stealth.apply_stealth_sync(page)
    yield page
    page.close()
