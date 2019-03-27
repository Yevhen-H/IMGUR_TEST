from selenium import webdriver
driver = webdriver.Chrome()#Firefox: executable_path="C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/geckodriver.exe"
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from new_post import New_Post


class Base_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def home_page(self):
        driver = self.driver
        driver.get("https://imgur.com/")

    def sign_in(self, user, password):
        driver = self.driver
        driver.find_element_by_css_selector("a.Navbar-signin").click()
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_name("submit").click()

    def random_mode(self):
        driver = self.driver
        driver.find_element_by_css_selector("div.Dropdown.sort.Dropdown--upper").click()
        driver.find_element_by_xpath("//span[2]/div/div[2]/div[2]/div[3]").click()

    def search_by_topic(self, search_word):
        driver = self.driver
        driver.find_element_by_css_selector("input.Searchbar-textInput").send_keys(search_word)
        driver.find_element_by_css_selector("button.Searchbar-submitInput").click()
        # click by picture
        driver.find_element_by_id("QSymA").click()
        # click next
        driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()

    def new_post(self, new_post):
        driver = self.driver
        driver.find_element_by_css_selector("span.Button-label").click()
        driver.find_element_by_css_selector("label.browse-btn").click()
        driver.find_element_by_css_selector("label.browse-btn").send_keys(new_post.path)
        # create title
        driver.find_element_by_css_selector("h1.post-title.post-contenteditable::before").send_keys(new_post.title)
        driver.find_element_by_css_selector("a.post-options-publish.btn.btn-action").click()

    def sign_out(self):
        driver = self.driver
        dropdown = driver.find_element_by_css_selector("a.topbar-icon.account-user-name")
        hover = ActionChains(driver).move_to_element(dropdown)
        hover.perform()
        driver.find_element_by_css_selector("button.log-out").click()

    def test_new_post(self):
        self.home_page()
        self.sign_in(user="SomeNewUser", password="secret1")
        self.test_new_post(new_post(path="C:/Users/yhurt/image1.png", title="cat and the glass"))
        self.sign_out()

    def test_search_by_topic(self):
        self.home_page()
        self.search_by_topic("space")

    def test_random_mode(self):
        self.home_page()
        self.random_mode()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()