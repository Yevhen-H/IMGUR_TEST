from selenium import webdriver
driver = webdriver.Chrome()  # replace on Firefox if needed
import time



driver.implicitly_wait(5)
driver.get("https://imgur.com/")
driver.find_element_by_css_selector("a.Navbar-signin").click()
#login
driver.find_element_by_id("username").send_keys("SomeNewUser")
driver.find_element_by_id("password").send_keys("secret1")
driver.find_element_by_name("submit").click()
#search by topic
driver.find_element_by_css_selector("input.Searchbar-textInput").send_keys("space")
driver.find_element_by_css_selector("button.Searchbar-submitInput").click()
#click by picture
driver.find_element_by_id("QSymA").click()
driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()
#write comment
driver.find_element_by_css_selector("spin.textarea.commentForm").send_keys("It is Awesome!")
#driver.find_element_by_css_selector("button.post-action-icon post-action-favorite icon-favorite-outline").click()
#
#driver.find_element_by_id("submit-comment").click()
time.sleep(8)