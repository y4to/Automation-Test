import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPortalDetails:
    URL = "https://webdriveruniversity.com/"
    EXPECTED_TITLE = "WebDriverUniversity.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        assert self.EXPECTED_TITLE in self.driver.title

    def alert_accept(self):
        alert = WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        print("\n", alert.text)
        time.sleep(1)
        alert.accept()

    def login_portal_button_ui(self):
        login_portal_button_ui = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, "login-portal"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_portal_button_ui)
        self.driver.execute_script("arguments[0].click();", login_portal_button_ui)

    #Clicking Login with INCORRECT fields
    def login_field_incorrect_correct(self):
        self.login_portal_button_ui()

        # SWITCH TO CONTACT US WINDOW
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

        #INCORRECT DETAILS
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "text"))).send_keys("gheian11")
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "password"))).send_keys("gheian11")
        time.sleep(1)

        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        self.alert_accept()

        #CORRECT DETAILS
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "text"))).send_keys("webdriver")
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "password"))).send_keys("webdriver123")
        time.sleep(1)

        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        self.alert_accept()

        #CLICK HOME
        self.driver.find_element(By.ID, "home-link").click()
        time.sleep(1)



