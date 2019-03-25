from selenium import webdriver
driver = webdriver.Chrome()
import time

driver.implicitly_wait(5)
driver.get("https://imgur.com/")
driver.find_element_by_css_selector("a.ButtonLink.Button.Navbar-signup").click()
driver.find_element_by_id("username").send_keys("SomeNewUser01")
driver.find_element_by_id("email").send_keys("yevenh@gmail.com")
driver.find_element_by_id("password").send_keys("secret1")
driver.find_element_by_id("confirm_password").send_keys("secret1")
driver.find_element_by_name("next").click()
#driver.find_element_by_css_selector("div.recaptcha-checkbox-checkmark").click()

time.sleep(8)
#driver.find_element_by_css_selector("input#username.br5.lvl1-dark.valid").send_keys("SomeNewUser")
#driver.find_element_by_css_selector("input#email.br5.lvl1-dark.valid").click()
#driver.find_element_by_css_selector("input#password.br5.lvl1-dark.valid").click()
#driver.find_element_by_css_selector("a.Navbar-signin").click()


#driver.quit()