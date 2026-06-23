import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys


class ToDoList:
    URL = "https://webdriveruniversity.com/"
    EXPECTED_TITLE = "WebDriverUniversity.com"

    new_to_do = ["hit the gym", "take protein", "drink water"]

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        assert self.EXPECTED_TITLE in self.driver.title

    def to_do_list_ui(self):
        to_do_list_button_ui = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, "to-do-list"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", to_do_list_button_ui)
        self.driver.execute_script("arguments[0].click();", to_do_list_button_ui)

        # SWITCH TO CONTACT US WINDOW
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

    #ADD OPTION, STRIKE 3 OPTIONS, THEN DELETE ALL, AND CLICK HOME
    def add_strike_remove(self):
        self.to_do_list_ui()

        #ADD IN TO DO LIST
        for things in self.new_to_do:
            new_things = self.driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']")
            new_things.send_keys(things + Keys.ENTER)
            time.sleep(1)

        #CLICK THE STRIKETHROUGH
        strikethrough_things = self.driver.find_elements(By.XPATH, "//div[@id='container']//ul/li")
        for each in range(3):
            click_strikethrough = strikethrough_things[each]
            click_strikethrough.click()
            time.sleep(1)

        #REMOVE FROM TO DO LIST
        remove_things = self.driver.find_elements(By.XPATH, "//div[@id='container']//ul/li")
        for click_remove in remove_things:
            click_remove.find_element(By.XPATH, "//i[@class='fa fa-trash']").click()
            time.sleep(1)

        #CLICK HOME
        self.driver.find_element(By.ID, "home-link").click()
        time.sleep(1)

