import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import invisibility_of_element
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def test_sort(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    assert "GreenKart" in driver.title, "Page title does not match!"

    BrowserSortedVeg = []

    # click on cloumn header
    driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()

    # to collect vegitable details
    SelSortedVeg = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-of-type(1)")

    for ele in SelSortedVeg:
        BrowserSortedVeg.append(ele.text)

    newveglist = BrowserSortedVeg.copy()

    BrowserSortedVeg.sort()

    assert newveglist == BrowserSortedVeg