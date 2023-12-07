# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import matplotlib.pyplot as plt

# for i in range(1, 2):
#     url = f'https://www.naukri.com/computer-science-jobs-{i}'

#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

#     try:
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get(url)
#         time.sleep(5)
#         html_doc = driver.page_source

#         soup = BeautifulSoup(html_doc, 'html.parser')


#         titles = []
#         companies = []
#         locations = []
#         experiences = []
#         salaries = []
#         skills = []
#         job_desc = []

#         for data in soup.findAll('div', class_='cust-job-tuple layout-wrapper lay-2 sjw__tuple'):
#             title = data.find('div', class_='row1')
#             company_name = data.find('span', class_='comp-dtls-wrap')
#             location = data.find('span', class_='loc-wrap ver-line')
#             experience = data.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-experience exp')
#             salary = data.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal')
#             skill = ', '.join(tag.text.strip() for tag in data.select('ul.tags-gt li.tag-li'))
#             desc = data.find('div', class_='row4')


#             titles.append(title.text.strip() if title else None)
#             companies.append(company_name.text.strip() if company_name else None)
#             locations.append(location.text.strip() if location else None)
#             experiences.append(experience.text.strip() if experience else None)
#             salaries.append(salary.text.strip() if salary else None)
#             skills.append(skill)
#             job_desc.append(desc.text.strip() if desc else None)
            
#         print(f"{i} is Executed")
        
#     finally:
#         driver.quit()


# # df = pd.DataFrame({'Title': titles, 'Companies': companies, 'Location': locations, 'experience': experiences,'salary': salaries, 'Description': job_desc})

# # df.to_excel('Naukricom.xlsx', index=True)


# # print(job_desc)
# # print(companies)
# # print(locations)
# # print(experience)
# # print(salaries)
# # print(job_desc)

# print(skills)

# programming_skills = []
# web_development_skills = []
# database_development_skills = []




with open('req_skills/Programming_Languages.txt') as a:
    all_prog_skills = a.readlines()
programming_skills = [skills.strip() for skills in all_prog_skills if skills.strip()]
# print(programming_skills)


with open('req_skills/web_development.txt') as s:
    all_web_skills = s.readlines()
web_development_skills = [skills.strip() for skills in all_web_skills if skills.strip()]
# print(web_development_skills)


with open ('req_skills/database_management.txt') as d:
    all_dbms_skills = d.readlines()
database_development_skills = [skills.strip() for skills in all_dbms_skills if skills.strip()]
# print(database_development_skills)

with open ('req_skills/version_control.txt') as f:
    all_version_control_skills = f.readlines()
version_control_skills = [skill.strip() for skill in all_version_control_skills if skill.strip()]
# print(version_control_skills)

with open ('req_skills/ide.txt') as g:
    all_ide_skills = g.readlines()
ide_skill = [skill.strip() for skill in all_ide_skills if skill.strip()]
# print(ide_skill)

with open('req_skills/devops.txt') as h:
    all_devops_skills = h.readlines()
devops_skills = [skill.strip() for skill in all_devops_skills if skill.strip()]
# print(devops_skills)

with open('req_skills/testing.txt') as j:
    all_testing_skills = j.readlines()
testing_skill = [skill.strip() for skill in all_testing_skills if skill.strip()]
# print(testing_skill)

with open ('req_skills/api_web_services.txt') as k:
    all_api_skills = k.readlines()
api_skill = [skill.strip() for skill in all_api_skills if skill.strip()]
# print(api_skill)

with open ('req_skills/frameworks.txt') as k:
    all_framework_skills = k.readlines()
framework_skills = [skill.strip() for skill in all_framework_skills if skill.strip()]
# print(framework_skills)

with open ('req_skills/cloud.txt') as k:
    all_android_development_skills = k.readlines()
android_development_skills = [skill.strip() for skill in all_android_development_skills if skill.strip()]
# print(android_development_skills)

with open ('req_skills/scripting.txt') as l:
    all_scripting_skills = l.readlines()
scripting_skills = [skill.strip() for skill in all_scripting_skills if skill.strip()]

with open ('req_skills/dsa.txt') as m:
    all_dsa_skills = m.readlines()
dsa_skills = [skill.strip() for skill in all_dsa_skills if skill.strip()]

with open ('req_skills/security.txt') as n:
    all_security_skills = n.readlines()
security_skill = [skill.strip() for skill in all_security_skills if skill.strip()]

with open ('req_skills/ai_machine_learning.txt') as b:
    all_ai_machine_lerning = b.readlines()
ai_machine_lerning = [skill.strip() for skill in all_ai_machine_lerning if skill.strip()]
# print(ai_machine_lerning)

with open ('req_skills/game_development.txt') as v:
    all_game_development_skills = v.readlines()
game_development_skills = [skill.strip() for skill in all_game_development_skills if skill.strip()]
# print(game_development_skills)

with open ('req_skills/design.txt') as c:
    all_design_skills = c.readlines()
design_skills = [skill.strip() for skill in all_design_skills if skill.strip()]
print(design_skills)

