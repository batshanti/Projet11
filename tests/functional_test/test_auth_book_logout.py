from selenium import webdriver
from selenium.webdriver.common.by import By


def test_auth_book_logout():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:5000/')
    assert driver.current_url == "http://127.0.0.1:5000/"

    input_email = driver.find_element(by=By.ID, value="email")
    input_email.send_keys("john@simplylift.co")
    submit_email = driver.find_element(by=By.TAG_NAME, value="button")
    submit_email.click()

    assert driver.current_url == 'http://127.0.0.1:5000/showSummary'
    assert "Welcome, john@simplylift.co" in driver.page_source

    book_competition = driver.find_element(by=By.CSS_SELECTOR, value='ul > li > a')
    book_competition.click()

    assert driver.current_url == "http://127.0.0.1:5000/book/Spring%20Festival/Simply%20Lift"

    required_places = driver.find_element(by=By.ID, value='required_places')
    required_places.send_keys('1')

    submit_places = driver.find_element(by=By.ID, value="submit")
    submit_places.click()

    assert driver.current_url == "http://127.0.0.1:5000/purchasePlaces"
    assert "Great-booking complete" in driver.page_source

    logout = driver.find_element(by=By.LINK_TEXT, value='Logout')
    logout.click()

    assert driver.current_url == "http://127.0.0.1:5000/"
    assert "Welcome to the GUDLFT Registration Portal!" in driver.page_source