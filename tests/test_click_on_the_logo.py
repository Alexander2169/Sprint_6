import allure
from conftest import driver
from page_objects.main_page import MainPage
from config import DZEN_URL

class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу "Яндекс.Самокат" при нажатии на логотип "Самокат"')
    def test_go_to_main_page_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзен"')
    def test_checking_the_transition_to_the_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert 'dzen.ru' in DZEN_URL



