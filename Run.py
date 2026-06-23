import pytest
from selenium import webdriver
from Call.HomePage import HomePage
from Call.ContactUs import ContactUsDetails
from Call.LoginPortal import LoginPortalDetails
from Call.ButtonClicks import ButtonClicks
from Call.ToDoList import ToDoList

@pytest.fixture
def driver():
    """Fixture to initialize and quit the browser."""
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_scroll(driver):
    page = HomePage(driver)
    page.open()
    page.scroll_page()


def test_logo_button(driver):
    page = HomePage(driver)
    page.open()
    page.click_logo()


def test_course_button(driver):
    page = HomePage(driver)
    page.open()
    page.click_course()

def test_contact_us(driver):
    contact_page = HomePage(driver)
    contact_page.open()
    contact_page.click_contact_us()

def test_login(driver):
    page = HomePage(driver)
    page.open()
    page.click_login()


def test_button_click(driver):
    page = HomePage(driver)
    page.open()
    page.click_button_click()


def test_to_do(driver):
    page = HomePage(driver)
    page.open()
    page.click_to_do()


def test_object_model(driver):
    page = HomePage(driver)
    page.open()
    page.click_object_model()


def test_card_link(driver):
    page = HomePage(driver)
    page.open()
    page.click_card_link()


def test_drop_check_radio(driver):
    page = HomePage(driver)
    page.open()
    page.click_drop_check_radio()


def test_ajax_loader(driver):
    page = HomePage(driver)
    page.open()
    page.click_ajax_loader()


def test_actions(driver):
    page = HomePage(driver)
    page.open()
    page.click_actions()


def test_scroll_around(driver):
    page = HomePage(driver)
    page.open()
    page.click_scroll_around()


def test_popup_alerts(driver):
    page = HomePage(driver)
    page.open()
    page.click_popup_alerts()


def test_iframes(driver):
    page = HomePage(driver)
    page.open()
    page.click_iframe()


def test_hidden_elements(driver):
    page = HomePage(driver)
    page.open()
    page.click_hidden_elements()


def test_data_table(driver):
    page = HomePage(driver)
    page.open()
    page.click_data_tables()

def test_autocomplete_textfield(driver):
    page = HomePage(driver)
    page.open()
    page.click_autocomplete_textfield()

def test_file_upload(driver):
    page = HomePage(driver)
    page.open()
    page.click_file_upload()

def test_datepicker(driver):
    page = HomePage(driver)
    page.open()
    page.click_datepicker()

def test_ai_playground(driver):
    page = HomePage(driver)
    page.open()
    page.click_ai_playground()


#Contact Us Details
def test_contact_us_details(driver):
    ContactUsDetails(driver).open()
    ContactUsDetails(driver).contact_page_filled()

def test_contact_us_empty(driver):
    ContactUsDetails(driver).open()
    ContactUsDetails(driver).contact_page_empty()

#Login Portal
def test_login_portal_incorrect_correct(driver):
    LoginPortalDetails(driver).open()
    LoginPortalDetails(driver).login_field_incorrect_correct()


#Button Clicks
def test_button_clicks(driver):
    ButtonClicks(driver).open()
    ButtonClicks(driver).web_element_click()

def test_js_clicks(driver):
    ButtonClicks(driver).open()
    ButtonClicks(driver).js_click()

def test_action_move_clicks(driver):
    ButtonClicks(driver).open()
    ButtonClicks(driver).action_move_click()

#To Do List
def test_new_to_do(driver):
    ToDoList(driver).open()
    ToDoList(driver).add_strike_remove()