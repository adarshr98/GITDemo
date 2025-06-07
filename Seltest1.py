import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@type ='submit']").click()
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
dropdown.select_by_value("az")

products = driver.find_elements(By.CLASS_NAME,"inventory_item")

for product in products:
    #item = product.find_element(By.CLASS_NAME,"inventory_item_name ").text
    item = product.find_element(By.CSS_SELECTOR, "div > div > a > div").text  #chaining
    if item in ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]:
        #product.find_element(By.XPATH, ".btn_primary").click()
        product.find_element(By.XPATH,"div/div[2]/button").click()

driver.find_element(By.XPATH,"//div[@id= 'shopping_cart_container']").click()
driver.find_element(By.XPATH,"//button[text() = 'Checkout']").click()

FirstName = "Adarsh"
LastName = "Ravichandran"
ZipCode = "001"

driver.find_element(By.ID,"first-name").send_keys(FirstName)
driver.find_element(By.ID, "last-name").send_keys(LastName)
driver.find_element(By.ID,"postal-code").send_keys(ZipCode)

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@type = 'submit']"))).click()
Total = driver.find_elements(By.CLASS_NAME,"inventory_item_price")

sum = 0
for Totals in Total:
    value = float(Totals.text.replace("$", ""))
    sum = sum + value

print(sum)

Tax = driver.find_element(By.CLASS_NAME,"summary_tax_label").text
print(Tax)

Tax = float(Tax.replace("Tax: $", "").strip())

assert Tax < sum

driver.find_element(By.XPATH,"//button[@id = 'finish']").click()
Order_placed = driver.find_element(By.TAG_NAME,"h2").text
print(Order_placed)
Order_msg = driver.find_element(By.CSS_SELECTOR,".complete-text").text
print(Order_msg)

assert "dispatched" in Order_msg