from selenium import webdriver
from selenium.webdriver.common.by import By


def test_auth():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:5000/')
    assert driver.current_url == "http://127.0.0.1:5000/"

    input_email = driver.find_element(by=By.ID, value="email")
    input_email.send_keys("john@simplylift.co")
    submit_email = driver.find_element(by=By.TAG_NAME, value="button")
    submit_email.click()

    assert driver.current_url == 'http://127.0.0.1:5000/showSummary'
    assert "Welcome, john@simplylift.co" in driver.page_source


