from pages.base_page import BasePage


class Jobs(BasePage):
    def get_tagline_text(self):
        tagline = self.driver.find_element_by_id('tagLine')
        return tagline.text