import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="function")
def driver():
    print ('\stsrt')
    driver = webdriver.Chrome()
    yield driver
    print ('\quit')
    driver.quit()