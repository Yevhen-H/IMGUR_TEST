from selenium import webdriver
driver = webdriver.Chrome() #Firefox: executable_path="C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/geckodriver.exe"
import time


driver.implicitly_wait(7)
driver.maximize_window()
driver.get("https://imgur.com/")
#randome mode
driver.find_element_by_css_selector("div.Dropdown.sort.Dropdown--upper").click()
driver.find_element_by_xpath("//span[2]/div/div[2]/div[2]/div[3]").click()
time.sleep(3)

