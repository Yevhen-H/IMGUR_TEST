from selenium import webdriver
import unittest
from page_objects.homepage import HomePage
from page_objects.search_page_result import SearchPageResult

#def test_new_post(base):
   # base.home_page()
    #base.new_post(New_Post(path="../res/test_image.png", title="cat and the glass"))


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../res/chromedriver.exe")
        #self.driver = webdriver.Firefox("../res/geckodriver.exe")

    def test_search_by_topic(self):
        test_search_word = "space"

        home_page = HomePage(self.driver)
        home_page.navigate_to_home_page()
        home_page.search_by_topic(test_search_word)
        search_page_result = SearchPageResult(self.driver)
        search_page_result.click_on_image()

        tags_list = search_page_result.get_tags()

        assert test_search_word in tags_list


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



# def test_random_mode(base):
#     base.home_page()
#     base.random_mode()
