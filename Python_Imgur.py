from selenium import webdriver
driver = webdriver.Chrome()#Firefox: executable_path="C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/geckodriver.exe"
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time


class Python_Imgur(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def home_page(self, driver):
        driver.get("https://imgur.com/")

    def test_sign_in(self, driver, user, password):
        driver.find_element_by_css_selector("a.Navbar-signin").click()
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_name("submit").click()

    def test_random_mode(self,driver):
        driver.find_element_by_css_selector("div.Dropdown.sort.Dropdown--upper").click()
        driver.find_element_by_xpath("//span[2]/div/div[2]/div[2]/div[3]").click()
    time.sleep(4)


    def test_search_by_topic(self, driver, search_word):
        driver.find_element_by_css_selector("input.Searchbar-textInput").send_keys(search_word)
        driver.find_element_by_css_selector("button.Searchbar-submitInput").click()
        # click by picture
        driver.find_element_by_id("QSymA").click()
        # click next
        driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()
    time.sleep(4)


    #def test_new_post(os_path, post_title):
        # create a new post
        # driver.find_element_by_css_selector("span.Button-label").click()
        # driver.find_element_by_css_selector("label.browse-btn").click()
        #driver.find_element_by_css_selector("label.browse-btn").send_keys(os_path)
        # create title
        #driver.find_element_by_css_selector("h1.post-title.post-contenteditable::before").send_keys(post_title)
        # driver.find_element_by_css_selector("a.post-options-publish.btn.btn-action").click()


    #test_new_post("C:/Users/yhurt/image1.png", "cat and the glass")


    def sign_out(self, driver):
        # sign ou
        dropdown = driver.find_element_by_css_selector("a.topbar-icon.account-user-name")
        hover = ActionChains(driver).move_to_element(dropdown)
        hover.perform()
        driver.find_element_by_css_selector("button.log-out").click()



    def test_methods(self,):

        self.home_page(driver)
        self.test_sign_in(driver, user="SomeNewUser", password="secret1")
        self.test_random_mode(driver)
        self.test_search_by_topic(driver, "space")
        self.sign_out(driver)
        self.test_methods()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()