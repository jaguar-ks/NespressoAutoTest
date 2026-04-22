from pages import LoginPage
from playwright.sync_api import expect

class TestLogin:
    def test_invalid_login_credentials(self, stealth_page, invalid_user_creds):
        login_page = LoginPage(stealth_page)
        login_page.navigate_to_login_page()
        login_page.entre_credentials(invalid_user_creds)
        login_page.submit_credentials()
        expect(
            login_page.get_alert_message()
        ).to_contain_text(
            "You did not sign in correctly or your account is temporarily disabled"
        )

    def test_valid_login_credentials(self, stealth_page, valid_user_creds):
        login_page = LoginPage(stealth_page)
        login_page.navigate_to_login_page()
        login_page.entre_credentials(valid_user_creds)
        login_page.submit_credentials()
        expect(
            login_page.get_text_under_user_icon()
        ).to_contain_text(
            "My Account"
        )