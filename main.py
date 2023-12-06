from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.naukri.com/computer-science-jobs-1'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    html_doc = driver.page_source

    soup = BeautifulSoup(html_doc, 'html.parser')
    
finally:
    driver.quit()


titles = []
companies = []
locations = []
experiences = []
salaries = []
job_desc = []


for data in soup.findAll('div', class_='cust-job-tuple layout-wrapper lay-2 sjw__tuple'):
    title = data.find('div', class_='row1')
    company_name = data.find('span', class_='comp-dtls-wrap')
    location = data.find('span', class_='loc-wrap ver-line')
    experience = data.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-experience exp')
    salary = data.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-experience exp')
    desc = data.find('div', class_='row4')


    titles.append(title.text.strip() if title else None)
    companies.append(company_name.text.strip() if company_name else None)
    locations.append(location.text.strip() if location else None)
    experiences.append(experience.text.strip() if experience else None)
    salaries.append(salary.text.strip() if salary else None)
    job_desc.append(desc.text.strip() if desc else None)




print(job_desc)
print(companies)
print(locations)
print(experience)
print(salaries)
print(job_desc)


