from pages.base_page import BasePage


class Homepage(BasePage):
    def navigate_to_jobs(self):
        jobs_link = self.driver.find_element_by_link_text('Join Us')
        jobs_link.click()