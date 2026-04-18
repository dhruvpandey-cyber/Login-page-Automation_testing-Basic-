from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "loginBtn")
        self.current_url = None

    def open(self, url):
        self.current_url = url
        self.driver.get(url)
        # Wait for username field to be visible
        self.wait.until(EC.presence_of_element_located(self.username))

    def login(self, user, pwd):
        username_field = self.wait.until(EC.presence_of_element_located(self.username))
        username_field.send_keys(user)
        
        password_field = self.wait.until(EC.presence_of_element_located(self.password))
        password_field.send_keys(pwd)
        
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_btn))
        login_button.click()
        
        # Wait for message to appear (either success or error)
        message_element = (By.ID, "message")
        self.wait.until(EC.visibility_of_element_located(message_element))