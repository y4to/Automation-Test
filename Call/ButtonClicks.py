import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class ButtonClicks:
    URL = "https://webdriveruniversity.com/"
    EXPECTED_TITLE = "WebDriverUniversity.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        assert self.EXPECTED_TITLE in self.driver.title

    def alert_close_button(self):
        alert_close = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@id='myModalClick']//button[@type='button'][normalize-space()='Close']")))
        print("\n", alert_close.text)
        time.sleep(1)
        alert_close.click()

    def alert_x_button(self):
        alert_x = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@id='myModalClick']//button[@type='button'][normalize-space()='×']")))
        print("\n", alert_x.text)
        time.sleep(1)
        alert_x.click()

    def alert_outside_space(self):
        alert_outside = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@id='myModalClick']")))
        time.sleep(1)
        alert_outside.click()

    def java_script_button(self):
        button_two = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//span[@id='button2']"))
        )
        self.driver.execute_script("arguments[0].click();", button_two)
        time.sleep(1)

    def action_move_button(self):
        action_move = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//span[@id='button3']"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(action_move).perform()

    def click_buttons_ui(self):
        button_click_button_ui = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, "button-clicks"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button_click_button_ui)
        self.driver.execute_script("arguments[0].click();", button_click_button_ui)

        # SWITCH TO CONTACT US WINDOW
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

    def web_element_click(self):
        self.click_buttons_ui()

        #WEB ELEMENT CLICK THEN CLOSE BY CLOSE BUTTON
        self.driver.find_element(By.XPATH, "//span[@id='button1']").click()
        time.sleep(1)

        self.alert_close_button()
        time.sleep(1)

        #WEB ELEMENT CLICK THEN CLOSE BY X BUTTON
        self.driver.find_element(By.XPATH, "//span[@id='button1']").click()
        time.sleep(1)

        self.alert_x_button()
        time.sleep(1)

        #WEB ELEMENT CLICK THEN CLOSE BY OUTSIDE SPACE
        self.driver.find_element(By.XPATH, "//span[@id='button1']").click()
        time.sleep(1)

        self.alert_outside_space()
        time.sleep(1)

    def js_click(self):
        self.click_buttons_ui()

        #JAVASCRIPT CLICK THEN CLOSE BY CLOSE BUTTON
        self.java_script_button()
        time.sleep(1)

        button_close = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@class='modal-dialog modal-md']//button[@type='button'][normalize-space()='Close']")))
        self.driver.execute_script("arguments[0].click();", button_close)
        print("\n", button_close.text)
        time.sleep(1)

        # JAVASCRIPT CLICK THEN CLOSE BY X BUTTON
        self.java_script_button()
        time.sleep(1)

        button_x = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@class='modal-dialog modal-md']//button[@type='button'][normalize-space()='×']")))
        self.driver.execute_script("arguments[0].click();", button_x)
        print("\n", button_x.text)
        time.sleep(1)

        # JAVASCRIPT CLICK THEN CLOSE BY OUTSIDE SPACE
        self.java_script_button()
        time.sleep(1)

        button_outside_space = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='myModalJSClick']")))
        self.driver.execute_script("arguments[0].click();", button_outside_space)
        time.sleep(1)

    def action_move_click(self):
        self.click_buttons_ui()

        #CLICK BUTTON USING ACTION MOVE CLICK
        self.action_move_button()
        time.sleep(1)

        #CLICK CLOSE USING ACTION MOVE CLICK
        close_move = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='myModalMoveClick']//button[@type='button'][normalize-space()='Close']"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(close_move).perform()
        time.sleep(1)

        #CLICK BUTTON USING ACTION MOVE CLICK
        self.action_move_button()
        time.sleep(1)

        #CLICK CLOSE USING ACTION X CLICK
        x_move = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//div[@id='myModalMoveClick']//button[@type='button'][normalize-space()='×']"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(x_move).perform()
        time.sleep(1)

        #CLICK BUTTON USING ACTION MOVE CLICK
        self.action_move_button()
        time.sleep(1)

        # CLICK CLOSE USING OUTSIDE SPACE
        outside_move = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//div[@id='myModalMoveClick']"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(outside_move).perform()
        time.sleep(1)



