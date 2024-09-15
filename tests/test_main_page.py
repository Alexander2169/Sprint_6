import allure
from page_objects.main_page import MainPage
from conftest import driver
from data import TestData
import pytest

class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка открытия соответствующего текста при нажатии на стрелочку')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_expected_answer_faq)
    def test_opening_the_corresponding_text_when_clicking_on_the_arrow(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq_answer(question_number) == expected_answer