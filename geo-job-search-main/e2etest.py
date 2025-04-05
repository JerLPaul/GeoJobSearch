import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class JobScrapingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Selenium WebDriver without headless mode to see the browser
        options = Options()
        cls.driver = webdriver.Chrome(options=options)
        
        cls.scraped_jobs = []
        with open('scrape/jobs.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                if i < 5:
                    cls.scraped_jobs.append(row)
                else:
                    break

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def standardize_text(self, text):
        return ' '.join(text.lower().split())

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page to ensure all lazy-loaded elements are displayed."""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def test_jobs_displayed_correctly(self):
        self.driver.get("http://localhost:3000/")
        
        # Scroll to the bottom of the page to ensure all jobs are loaded
        self.scroll_to_bottom()
        
        # Wait for the first job card's title to be loaded
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".card .card-title"))
        )
        
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        job_cards = soup.find_all(class_='card')
        displayed_job_titles = []
        for card in job_cards[:5]:  # Only consider the top 5 job cards
            title_element = card.find('div', class_='card-title')
            if title_element:
                title = self.standardize_text(title_element.text)
                displayed_job_titles.append(title)
        
        # Standardize the job titles for comparison from the .csv
        standardized_scraped_job_titles = set(
            self.standardize_text(job['Title']) for job in self.scraped_jobs
        )
        

        for title in displayed_job_titles:
            with self.subTest(title=title):
                self.assertIn(title, standardized_scraped_job_titles, f"{title} not found in scraped jobs")

if __name__ == "__main__":
    unittest.main()