from playwright.sync_api import Page, expect
from pages import HomePage
import re

def test_navigate_to_coffee_mugs(stealth_page: Page):
    home_page = HomePage(stealth_page)
    home_page.navigate_to_home_page()
    home_page.hover_accessories_item()
    home_page.select_coffee_mugs()
    expect(home_page.page).to_have_title(re.compile(r"^Travel Mugs"))
