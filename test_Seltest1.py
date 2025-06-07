import json
import time
from os import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest

from pageObjects.checkout import CheckoutPage
from pageObjects.checkoutComplete import CheckoutComplete
from pageObjects.checkoutOverview import CheckoutOverview
from pageObjects.login import LoginPage
from pageObjects.shoppage import ShopPage
from pageObjects.userdetails import UserDetails

test_data_path = "../data/test_Seltest1.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_sel(browserInstance, test_list_item):
    driver = browserInstance
    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    shoppage = loginpage.login(test_list_item["UserName"],test_list_item["UserPassword"])
    shoppage.shop(test_list_item["ProductName"])
    print(shoppage.getTitle())
    checkoutpage = shoppage.shop_cart()
    userdetails = checkoutpage.checkout()
    checkout_overview = userdetails.userinfo()
    checkout_overview.checkoutbilltotal()
    checkoutcomplete = checkout_overview.checkoutfinsh()
    checkoutcomplete.checkout_complete()