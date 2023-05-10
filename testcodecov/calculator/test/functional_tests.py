import unittest
from playwright.sync_api import sync_playwright
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestExample(StaticLiveServerTestCase):
    def test_example(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_context().new_page()

            # Navigate to your app
            page.goto(self.live_server_url + "/index.html")
            page.pause()

            # Perform some assertions or interactions with the page
            self.assertIn("frontend", page.title())

            browser.close()
