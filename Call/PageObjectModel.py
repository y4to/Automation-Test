import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys


class PageObjectModel:
    URL = "https://webdriveruniversity.com/"
    EXPECTED_TITLE = "WebDriverUniversity.com"

    new_to_do = ["hit the gym", "take protein", "drink water"]

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        assert self.EXPECTED_TITLE in self.driver.title

    def page_object_model_ui(self):
        page_object_model_button_ui = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, "page-object-model"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", page_object_model_button_ui)
        self.driver.execute_script("arguments[0].click();", page_object_model_button_ui)

        # SWITCH TO CONTACT US WINDOW
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

    def find_out_more_button(self):
            find_out_more = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@id='button-find-out-more']"))
            )
            action_click = ActionChains(self.driver)
            action_click.click(find_out_more).perform()
            time.sleep(1)

    def click_outside_fom(self):
        outside_fom = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//body"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(outside_fom).perform()
        time.sleep(1)

    def our_products_button(self):
        click_our_product_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Our Products']"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(click_our_product_button).perform()
        time.sleep(1)

    def home_pom(self):
        self.page_object_model_ui()

        #CAROUSEL RIGHT AND LEFT
        for r_times in range(3):
            carousel_move_right = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//span[@class='glyphicon glyphicon-chevron-right']"))
            )
            action_click = ActionChains(self.driver)
            action_click.click(carousel_move_right).perform()
            time.sleep(1)

        for l_times in range(4):
            carousel_move_right = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//span[@class='glyphicon glyphicon-chevron-left']"))
            )
            action_click = ActionChains(self.driver)
            action_click.click(carousel_move_right).perform()
            time.sleep(1)

        #RADIO BUTTONS
        radio_buttons = self.driver.find_elements(By.XPATH, "//ol[@class='carousel-indicators']//li")
        for radio_buttons_click in range(3):
            radio_click = radio_buttons[radio_buttons_click]
            radio_click.click()
            time.sleep(1)

        #CLICK NAV OPTIONS
        button_navigation = ["//a[normalize-space()='Contact Us']",
                             "//a[normalize-space()='Our Products']"]

        for each_nav_pages in button_navigation:
            click_navigation = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, each_nav_pages))
            )
            action_click = ActionChains(self.driver)
            action_click.click(click_navigation).perform()
            time.sleep(1)
            self.driver.back()
            time.sleep(1)

        #FIND OUT MORE BUTTON
        sources = ["//button[normalize-space()='Close']",
                   "//button[normalize-space()='×']",
                   "//button[normalize-space()='Find Out More']",
                   "//div[@id='myModal']"]
        for close_buttons in sources:
            self.find_out_more_button()

            fom_click = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, close_buttons))
            )
            action_click = ActionChains(self.driver)
            action_click.click(fom_click).perform()
            time.sleep(1)
            self.click_outside_fom()
            time.sleep(1)

    def our_products(self):
        self.our_products_button()

        product_list = ["//div[@id='container-special-offers']",
                        "//div[@id='container-product1']",
                        "//div[@id='container-product2']",
                        "//div[@id='container-product3']",
                        "//div[@id='container-product4']",
                        "//div[@id='container-product5']",
                        "//div[@id='container-product6']",
                        "//div[@id='container-product7']"]

        sources_op = ["//button[normalize-space()='Close']",
                      "//button[normalize-space()='×']",
                      "//button[normalize-space()='Proceed']",
                      "//div[@id='myModal']"]

        time.sleep(1)
        for list_products in product_list:
            for close_buttons in sources_op:

                #CLICK A PRODUCT AT A TIME
                click_products = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, list_products))
                )
                action_click = ActionChains(self.driver)
                action_click.click(click_products).perform()
                time.sleep(1)

                #CLICK ALL CLOSE BUTTON SOURCES
                op_click = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, close_buttons))
                )
                action_click = ActionChains(self.driver)
                action_click.click(op_click).perform()
                time.sleep(1)

        # SENT TO CONTACT US
        click_contact_us = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Contact Us']"))
        )
        action_click = ActionChains(self.driver)
        action_click.click(click_contact_us).perform()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        # SENT TO HOME
        click_home = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Home']"))
            )
        time.sleep(1)
        action_click = ActionChains(self.driver)
        action_click.click(click_home).perform()
        time.sleep(1)

        self.driver.close()