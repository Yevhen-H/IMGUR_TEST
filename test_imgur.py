import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestImgur(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/chromedriver.exe")
        self.driver.get("https://imgur.com/upload")

    def test_upload_pic(self):
        image_path = "C:/Users/yhurt/PycharmProjects/IMGUR_TEST/venv37/image2.png"
        self.driver.find_element_by_id("global-files-button").send_keys(image_path)
        upload_complete_message_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'FlipInfo-message')))
        self.assertIn("Upload complete", upload_complete_message_element.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

