from selenium import webdriver
driver = webdriver.Chrome() #Firefox: executable_path="C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/geckodriver.exe"
import time
from selenium.webdriver.common.action_chains import ActionChains


driver.implicitly_wait(7)
driver.maximize_window()
driver.get("https://imgur.com/")
#sign in
driver.find_element_by_css_selector("a.Navbar-signin").click()
driver.find_element_by_id("username").send_keys("SomeNewUser")
driver.find_element_by_id("password").send_keys("secret1")
driver.find_element_by_name("submit").click()
#search by topic
driver.find_element_by_css_selector("input.Searchbar-textInput").send_keys("space")
driver.find_element_by_css_selector("button.Searchbar-submitInput").click()
#click by picture
driver.find_element_by_id("QSymA").click()
#click next
driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()
time.sleep(5)
#sign out
dropdown = driver.find_element_by_css_selector("a.topbar-icon.account-user-name")
hover = ActionChains(driver).move_to_element(dropdown)
hover.perform()
driver.find_element_by_css_selector("button.log-out").click()
driver.quit()