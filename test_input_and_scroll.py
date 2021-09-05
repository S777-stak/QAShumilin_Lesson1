from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

def test_input_and_scroll():
    driver = Chrome("C:/Users/user/PycharmProjects/pythonProject/Lesson_17/drivers/chromedriver.exe")
    driver.implicitly_wait(5)

    search_input_field_locator = "//input[@placeholder='Искать']"
    result_link_locator = "//div class="" style="">×</div>"

    driver.get("https://elmir.ua/")
    driver.maximize_window()

    search_input_field: WebElement = driver.find_element_by_xpath(search_input_field_locator)
    search_input_field.send_keys("ноутбук")
    search_input_field.send_keys(Keys.ENTER)

    driver.execute_script("window.scrollTo(0, 600)")

    first_link: WebElement = driver.find_element_by_xpath(result_link_locator)
    first_link.click()

    driver.quit()