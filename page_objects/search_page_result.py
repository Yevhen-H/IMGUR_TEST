
class SearchPageResult:

    # locators

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def click_on_image(self):
        driver = self.driver
        driver.find_element_by_id("QSymA").click()
        # # click next
        # driver.find_element_by_css_selector("div.btn.btn-action.navNext").click()

    def get_tags(self):
        driver = self.driver
        list_of_tags = []

        elements = driver.find_elements_by_class_name("post-tag-link")
        for tag in elements:
            for word in tag.text.split():
                list_of_tags.append(word)

        return list_of_tags
