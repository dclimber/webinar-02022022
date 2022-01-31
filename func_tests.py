from selenium import webdriver

PATH_TO_CHROME: str = './chromedriver'
browser = webdriver.Chrome(PATH_TO_CHROME)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
