from selenium import webdriver
driver = webdriver.Chrome()  # replace on Firefox if needed
import time
import os


driver.implicitly_wait(5)
driver.get("https://imgur.com/")
driver.find_element_by_css_selector("a.Navbar-signin").click()
#login
driver.find_element_by_id("username").send_keys("SomeNewUser")
driver.find_element_by_id("password").send_keys("secret1")
driver.find_element_by_name("submit").click()
#create a new post
driver.find_element_by_css_selector("span.Button-label").click()
fileinput = driver.find_element_by_css_selector("label.browse-btn").click()
driver.find_element_by_css_selector("label.browse-btn").send_keys("C:/Users/yhurt/image1.png")

#elm = driver.find_element_by_css_selector("label.browse-btn")
#elm.send_keys(os.getcwd() + "C:/Users/yhurt/image1.png")



#fileInput  = driver.find_element_by_css_selector("label.browse-btn")
#driver.execute_script("arguments[0].setAttribute('value', 'C:/Users/yhurt/image1.png')", fileInput)
#send_keys(os.getcwd()+"/image1.png")
time.sleep(10)

#create title
#driver.find_element_by_css_selector("h1.post-title.post-contenteditable::before").send_keys("cat and the glass")
#driver.find_element_by_css_selector("a.post-options-publish.btn.btn-action").click()

#sign out

#driver.find_element_by_css_selector("div.Dropdown-title").click()
#driver.find_element_by_css_selector("img.sign-out").click()



time.sleep(2)