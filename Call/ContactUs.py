import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ContactUsDetails:
    URL = "https://webdriveruniversity.com/"
    EXPECTED_TITLE = "WebDriverUniversity.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        assert self.EXPECTED_TITLE in self.driver.title

    def contact_us_button_ui(self):
        contact_us_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, "contact-us"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", contact_us_button)
        self.driver.execute_script("arguments[0].click();", contact_us_button)

    #IF FIELDS ARE NOT EMPTY
    def contact_page_filled(self):
        self.contact_us_button_ui()

        #SWITCH TO CONTACT US WINDOW
        self.driver.switch_to.window(self.driver.window_handles[1])

        #INPUT FIELDS
        def input_fields():
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "first_name"))).send_keys("John")
            time.sleep(1)

            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "last_name"))).send_keys("Doe")
            time.sleep(1)

            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "email"))).send_keys("john.doe@example.com")
            time.sleep(1)

            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "message"))).send_keys("This is a test message.")
            time.sleep(1)

        # Click Reset button
        input_fields()
        self.driver.find_element(By.XPATH, "//input[@value='RESET']").click()
        time.sleep(1)

        # Click Submit button
        input_fields()
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)

        #If Email format is CORRECT
        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Back to Homepage')]").click()
        time.sleep(1)

    #IF FIELDS ARE EMPTY
    def contact_page_empty(self):
        self.contact_us_button_ui()

        # SWITCH TO CONTACT US WINDOW
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Click Submit button
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)

        #Click Try Again
        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Try Again')]").click()
        time.sleep(1)

        # Click Submit button
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)

        #Click Home
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()
        time.sleep(1)



