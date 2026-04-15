from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_locked_user_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    username.send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    ).text

    assert "locked out" in error.lower()

    driver.quit()