from unittest import TestCase
from selenium import webdriver

from pages.homepage import Homepage
from pages.jobs import Jobs


class HomepageTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://uptake.com/')

    def tearDown(self):
        self.driver.close()

    def test_navigation_to_jobs_page(self):
        homepage = Homepage(self.driver)
        homepage.navigate_to_jobs()

        jobs = Jobs(self.driver)
        self.assertEqual(
            jobs.get_tagline_text(),
            'We’re looking for curious, nimble and passionate people.',
        )