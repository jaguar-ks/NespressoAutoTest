from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_list = page.locator("[class^='ui-menu ']")
        self.accessories_menu_item = page.locator("[class*='icon-accessories']")
        self.coffee_mugs = page.locator("[href$='travel-coffee-mugs']")

    def navigate_to_home_page(self):
        self.page.goto("https://www.nespresso.com/ma/fr")

    def hover_accessories_item(self):
        self.accessories_menu_item.hover()

    def select_coffee_mugs(self):
        self.coffee_mugs.click()

    def get_page_title(self):
        return self.page.title()