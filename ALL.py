from selenium import webdriver
driver = webdriver.Chrome()#Firefox: executable_path="C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/geckodriver.exe"
from selenium.webdriver.common.action_chains import ActionChains
import time

driver.implicitly_wait(5)


def home_page():
    driver.get("https://imgur.com/")
home_page()


def sign_in(user, password):
    driver.find_element_by_css_selector("a.Navbar-signin").click()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("submit").click()


sign_in(user="SomeNewUser", password="secret1")


def random_mode():
    driver.find_element_by_css_selector("div.Dropdown.sort.Dropdown--upper").click()
    driver.find_element_by_xpath("//span[2]/div/div[2]/div[2]/div[3]").click()
random_mode()
time.sleep(4)


def search_by_topic(search_word):
    driver.find_element_by_css_selector("input.Searchbar-textInput").send_keys(search_word)
    driver.find_element_by_css_selector("button.Searchbar-submitInput").click()
    # click by picture
    driver.find_element_by_id("QSymA").click()
    # click next
    driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()


search_by_topic("space")
time.sleep(4)


#def new_post(os_path, post_title):
    # create a new post
    # driver.find_element_by_css_selector("span.Button-label").click()
    # driver.find_element_by_css_selector("label.browse-btn").click()
    #driver.find_element_by_css_selector("label.browse-btn").send_keys(os_path)
    # create title
    #driver.find_element_by_css_selector("h1.post-title.post-contenteditable::before").send_keys(post_title)
    # driver.find_element_by_css_selector("a.post-options-publish.btn.btn-action").click()


#new_post("C:/Users/yhurt/image1.png", "cat and the glass")


def sign_out():
    # sign ou
    dropdown = driver.find_element_by_css_selector("a.topbar-icon.account-user-name")
    hover = ActionChains(driver).move_to_element(dropdown)
    hover.perform()
    driver.find_element_by_css_selector("button.log-out").click()

sign_out()
driver.quit()