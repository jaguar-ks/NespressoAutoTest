from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.locator("[placeholder='Email Address*']")
        self.pass_field = page.locator("[placeholder='Password*']")
        self.sign_in_button = page.locator("[class='action login primary']")

    def navigate_to_login_page(self):
        self.page.goto("https://www.nespresso.com/ma/en/customer/account/login/")

    def entre_credentials(self, user):
        self.email_field.fill(user['email'])
        self.pass_field.fill(user['password'])

    def submit_credentials(self):
        self.sign_in_button.click()
    
    def get_alert_message(self):
        alert_message = self.page.locator(".message-error")
        print(f"++++[{alert_message.text_content()}]++++")
        return alert_message
    
    def get_text_under_user_icon(self):
        text = self.page.locator(".header-account-link")
        print(f"++++[{text.text_content()}]++++")
        return text