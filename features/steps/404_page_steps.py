from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


DOG_IMG = (By.CSS_SELECTOR, "img[alt='Dogs of Amazon']")


@given('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    # print(f'Current window handle {context.original_window}')


@when('Click on a dog image')
def click_dog_img(context):
    context.driver.find_element(*DOG_IMG).click()
    context.driver.wait.until(EC.new_window_is_opened)


@when('Switch to new window')
def switch_window(context):
    all_window_handles = context.driver.window_handles # [0, 1]
    # print(all_window_handles)
    context.driver.switch_to.window(all_window_handles[1])
    # print(f'Current window handle (after switch): {context.driver.current_window_handle}')
