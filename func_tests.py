import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH_TO_CHROME: str = './chromedriver'


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(PATH_TO_CHROME)

    def tearDown(self):
        self.browser.quit()

    def test_can_use_a_contact_form_and_is_redirected_later(self):
        # Яна узнала, что его друг Декс создал себе сайт портфолио.
        # Она решила его посмотреть и открыла главную страницу.
        self.browser.get('http://localhost:8000')

        # Она увидела, что в заголовке сайта говорится, что это
        # портфолио Декса
        self.assertIn('Портфолио Декса', self.browser.title)

        # Яна увидела на сайте Декса контактную форму и решила написать ему
        # через неё, что она посмотрела его сайт.

        # Яна заполнила поле Full name своими ФИО
        input_full_name = self.browser.find_element_by_id('id_full_name')
        input_full_name.send_keys('Алматинская Яна Рфмшатовна')

        # Яна заполнила свой емейл
        input_email = self.browser.find_element_by_id('id_email')
        input_email.send_keys('yana@yandex.ru')

        # Яна заполнила номер телефона
        input_phone = self.browser.find_element_by_id('id_phone')
        input_phone.send_keys('+77779997777')

        # Яна написала сообщение Дексу:
        input_message = self.browser.find_element_by_id('id_message')
        input_message.send_keys('Декс, я посмотрела твой сайт, ты молодец!')

        # Яна нажала кнопку Send
        input_message.send_keys(Keys.ENTER)

        self.fail('Finish the test!')  # падает — напоминалка нам дописать тест
        # И её перебросило на страницу «Спасибо»

        # Довольная Яна ушла пить Шампанское.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
