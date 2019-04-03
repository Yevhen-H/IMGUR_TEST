from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(object):
    
    # locators
    sign_in_button = (By.CSS_SELECTOR, "a.Navbar-signin")
    username_locator = (By.ID, "username")

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def navigate_to_home_page(self):
        driver = self.driver
        driver.get("https://imgur.com/")

    def sign_in(self, user, password):
        driver = self.driver
        driver.find_element(self.sign_in_button)
        driver.find_element(self.username_locator).send_keys(user)
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

    def click_picture(self):
        driver = self.driver
        driver.find_element_by_id("QSymA").click()
        # click next
        driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()


    def new_post(self, new_post):
        driver = self.driver
        driver.find_element_by_css_selector("span.Button-label").click()
        driver.find_element_by_css_selector("label.browse-btn").click()
        image_path = "/Users/dpasichnyi/.pyenv/versions/imgur/image.png"
        driver.find_element_by_id("global-files-button").send_keys(image_path)
        # create title
        driver.find_element_by_css_selector("h1.post-title.post-contenteditable::before").send_keys(new_post.title)
        driver.find_element_by_css_selector("a.post-options-publish.btn.btn-action").click()

    def sign_out(self):
        driver = self.driver
        dropdown = driver.find_element_by_css_selector("a.topbar-icon.account-user-name")
        hover = ActionChains(driver).move_to_element(dropdown)
        hover.perform()
        driver.find_element_by_css_selector("button.log-out").click()

    def destroy(self):
        self.driver.close()

