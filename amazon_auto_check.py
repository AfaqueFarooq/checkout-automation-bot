from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
def amazon_auto_checkout(product_name, username, password):
    # set up the chrome WebDriver (you need to have chromedriver installed)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        # open amazon and navigate to the login page
        driver.get("https://www.amazon.com")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-nav-role, 'signin')]"))).click()
        
        #input email
        enter_email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@type, 'email')]")))
        enter_email.send_keys(username)
        enter_email.send_keys(Keys.RETURN)

        #input password
        enter_pass = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@type, 'password')]")))
        enter_pass.send_keys(password)
        enter_pass.send_keys(Keys.RETURN)

        # Search for the product
        search_pro = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@type, 'text')]")))
        search_pro.send_keys(product_name)
        search_pro.send_keys(Keys.RETURN)

        # Click on add to cart button
        element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='a-autoid-1-announce']"))
            )
        element.click()

        #navigate to proceed checkout page
        driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
        
        # Click on proceed checkout
        time.sleep(5) 
        checkout = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-feature-id='proceed-to-checkout-action']")))
        checkout.click()


        
        #click place order
        place_order = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-feature-id='proceed-to-checkout-action']"))
            )
        # place_order.click()

        # input()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()


product_name = input("Enter the product name: ")
amazon_username = input("Enter your Amazon username: ")
amazon_password = input("Enter your Amazon password: ")

amazon_auto_checkout(product_name, amazon_username, amazon_password)

