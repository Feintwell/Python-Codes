import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("website.URL")

login_button = driver.find_element(By.XPATH, "//header//a[contains(text(), 'Log in')]")
login_button.click()

email_field = driver.find_element(By.XPATH, "//input[@name='email' or @type='email']")
email_field.send_keys("your@email.here")

continue_button = driver.find_element(By.XPATH, "//button[contains(., 'Continue')]")
continue_button.click()

# Wait password field to appear
wait = WebDriverWait(driver, 10)
password_field = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='password' or @type='password']")))

password_field.send_keys("password")

submit_button = driver.find_element(By.XPATH, "//button[@type='submit' or contains(., 'Log in') or contains(., 'Continue')]")
submit_button.click()

inspections_menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//nav//span[text()='Inspections'] | //a[contains(., 'Inspections')]"))
)
inspections_menu.click()

start_inspection_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Start inspection')] | //a[contains(., 'Start inspection')]"))
)
start_inspection_btn.click()

input("Press Enter to close browser")
driver.quit()