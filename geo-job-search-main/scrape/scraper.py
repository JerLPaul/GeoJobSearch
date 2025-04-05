""" Module docstring """
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_job_title(jsoup):
    """Uses beautiful soup to get the job title"""
    title = jsoup.find('h1', {'class' : 'jobsearch-JobInfoHeader-title'})
    return title.text.strip() if title else "No Title Found"

def get_job_location(jsoup):
    """Uses beautiful soup to get the job location"""
    job_location = jsoup.find('div', {'data-testid' : 'inlineHeader-companyLocation'})
    return job_location.text.strip() if job_location else "No Location Found"

def get_company_name(jsoup):
    """Uses beautiful soup to get the company name"""
    company = jsoup.find('div', class_='jobsearch-CompanyInfoWithoutHeaderImage')
    return company.text.strip() if company else "No Company Found"

def get_job_salary(jsoup):
    """Uses beautiful soup to get the job salary"""
    salary = jsoup.find('div', {'id' : 'salaryInfoAndJobType'})
    if (not salary or not any(char.isdigit() for char in salary.text.strip())):
        return "No Salary Found"
    return salary.text.strip()

def get_job_summary(jsoup):
    """Uses beautiful soup to get the job summary"""
    summary = jsoup.find('div', {'id' : 'jobDescriptionText'})
    return summary.text.strip() if summary else "No Job Summary Found"

def get_job_cards(source):
    """ Printing function job cards """
    soup = BeautifulSoup(source, 'html.parser')
    return soup.find_all('div', class_='job_seen_beacon')

if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    TEMP_STRING = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    TEMP_STRING += " (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    options.add_argument(TEMP_STRING)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    SERVICE = webdriver.chrome.service.Service()
    driver = webdriver.Chrome(service=SERVICE, options=options)
    JOB_TITLE = "Software Engineer"
    LOCATION = "Ontario"
    # Open the indeed search page
    driver.get(f"https://ca.indeed.com/jobs?q={JOB_TITLE}&l={LOCATION}")
    time.sleep(5)
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_cards = get_job_cards(driver.page_source) #soup.find_all('div', class_='job_seen_beacon')
    with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Title', 'Company', 'Location', 'Summary', 'Link', 'Salary'])

        for job_card in job_cards:
            # Extract job link
            linkElement = job_card.find('a', href=True)

            if linkElement:
                JOB_LINK = f"https://ca.indeed.com{linkElement['href']}"
            else:
                JOB_LINK = "No Link Found"

            if JOB_LINK != 'No Link Found':
                print("Accessing link: " + JOB_LINK)
                # Navigate to the job link
                driver.get(JOB_LINK)
                # Wait for the job page to load
                time.sleep(2)
                # Parse the job page
                job_soup = BeautifulSoup(driver.page_source, 'html.parser')
                TITLE = get_job_title(job_soup)
                COMPANY = get_company_name(job_soup)
                LOCATION = get_job_location(job_soup)
                SUMMARY = get_job_summary(job_soup)
                SALARY = get_job_salary(job_soup)
            else:
                TITLE = COMPANY = LOCATION = SUMMARY = SALARY = 'No Data Found'
            # Write the job details to the CSV file
            writer.writerow([TITLE, COMPANY, LOCATION, SUMMARY, JOB_LINK, SALARY])
    driver.quit()  # Close the browser after fetching all the job details
    print("Job details saved to jobs.csv")
