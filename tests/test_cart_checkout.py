from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_and_checkout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    username.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.url_contains("cart"))

    driver.find_element(By.ID, "checkout").click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("Aditya")
    driver.find_element(By.ID, "last-name").send_keys("Test")
    driver.find_element(By.ID, "postal-code").send_keys("226001")
    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    success = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert "thank you" in success.lower()

    driver.quit()
    