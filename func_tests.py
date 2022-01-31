import unittest

from selenium import webdriver

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

        self.fail('Finish the test!')  # падает — напоминалка нам дописать тест

        # Яна увидела на сайте Декса контактную форму и решила написать ему
        # через неё, что она посмотрела его сайт.

        # Яна заполнила поле Full name своими ФИО - Алматинская Яна Рфмшатовна

        # Яна заполнила свой емейл: yana@yandex.ru

        # Яна заполнила номер телефона: +77779997777

        # Яна написала сообщение Дексу:
        # Декс, я посмотрела твой сайт, ты молодец!

        # Яна нажала кнопку Send

        # И её перебросило на страницу «Спасибо»

        # Довольная Яна ушла пить Шампанское.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
