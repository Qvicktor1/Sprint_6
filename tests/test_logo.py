import allure
from common_data import Urls
from pages.home_page import HomePage
from locators.base_page_locators import BasePageLocators as Bpl
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators as Opl


class TestLogoRedirect:

    @allure.title('Test of Яндекс logo redirect')
    @allure.description('Checking that clicking on the Яндекс logo redirects to the Dzen home page')
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.click_element(Bpl.yandex_logo_header)
        home_page.switch_to_tab()
        current_url = home_page.get_current_page_url()
        assert current_url == Urls.dzen_url, f"Failed to redirect to {Urls.dzen_url}"

    @allure.title('Test of Самокат logo redirect')
    @allure.description('Checking that clicking on the Самокат logo redirects to the Самокат home page')
    def test_samokat_logo_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.click_element(Bpl.order_button_header)
        order_page = OrderPage(driver)
        order_page.check_element_is_visible(Opl.user_form_header)
        order_page.click_element(Bpl.samokat_logo_header)
        home_page_url = home_page.get_current_page_url()
        assert home_page_url == Urls.main_url, f"Failed to return to home page"