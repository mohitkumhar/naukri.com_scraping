# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
import matplotlib.pyplot as plt
import io

# for i in range(1, 3):
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
#             skill = ', '.join(tag.text.strip() for tag in data.select('ul.tags-gt li.tag-li'))
#             location = data.find('span', class_='loc-wrap ver-line')
#             experience = data.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-experience exp')
#             salary = data.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal')
#             desc = data.find('div', class_='row4')


#             titles.append(title.text.strip() if title else None)
#             companies.append(company_name.text.strip() if company_name else None)
#             skills.append(skill)
#             locations.append(location.text.strip() if location else None)
#             experiences.append(experience.text.strip() if experience else None)
#             salaries.append(salary.text.strip() if salary else None)
#             job_desc.append(desc.text.strip() if desc else None)
            
#         print(f"{i} is Executed")
        
#     finally:
#         driver.quit()


# df = pd.DataFrame({'Title': titles, 'Companies': companies, 'Skills': skills, 'Location': locations, 'experience': experiences,'salary': salaries, 'Description': job_desc})

# df.to_excel('Naukricom.xlsx', index=True)


# # print(job_desc)
# # print(companies)
# # print(skills)
# # print(locations)
# # print(experience)
# # print(salaries)
# # print(job_desc)





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
# print(design_skills)

with open ('req_skills/networking.txt') as c:
    all_networking_skills = c.readlines()
networking_skills = [skill.strip() for skill in all_networking_skills if skill.strip()]
# print(networking_skills)

with open ('req_skills/os.txt') as c:
    all_os_skills = c.readlines()
os_skills = [skill.strip() for skill in all_os_skills if skill.strip()]
# print(os_skills)

with open ('req_skills/collaboration_tools.txt') as c:
    all_collaboration_tools_skills = c.readlines()
collaboration_tools_skills = [skill.strip() for skill in all_collaboration_tools_skills if skill.strip()]
# print(collaboration_tools_skills)

with open ('req_skills/soft_skill.txt') as c:
    all_soft_skills = c.readlines()
soft_skills = [skill.strip() for skill in all_soft_skills if skill.strip()]
# print(soft_skills)





all_skills  = programming_skills + web_development_skills + database_development_skills + version_control_skills + ide_skill + devops_skills + testing_skill + api_skill + framework_skills + android_development_skills + scripting_skills + dsa_skills + security_skill + ai_machine_lerning + game_development_skills + design_skills + networking_skills + os_skills + collaboration_tools_skills + soft_skills
print(all_skills)

skills = ['C' ,'Programming', 'Java', 'C++', 'Ca', 'C', 'Artificial Intelligence', 'Machine Learning', 'C']


programming_pie = [programming_skills.count(skill) for skill in skills]
print(programming_pie)

non_zero_index = [i for i, count in enumerate(programming_pie) if count > 0]
print(non_zero_index)

label = [skills[skill] for skill in non_zero_index]
print(label)

skill_count = {}
for language in label:
    skill_count[language] = skill_count.get(language, 0) + 1
print(skill_count)

pie_content = []


for i in skill_count:
    pie_content.append(skill_count.get(i))
print(pie_content)

dark_colors = [
    'steelblue', 'darkorange', 'darkgreen', 'firebrick',
    'rebeccapurple', 'saddlebrown', 'mediumvioletred', 'dimgray',
    'darkolivegreen', 'teal', 'slateblue', 'coral',
    'teal', 'purple', 'teal', 'darkred',
    'hotpink', 'green', 'saddlebrown', 'slategray'
    ]
color = []

for i in range(0, len(pie_content)):
    color.append(dark_colors[i])
print(f"colors: {color}")

explodes = [0, 0.1, 0, 0, 0, 0, 0.2, 0, 0]
explode=[]

for i in range(0, len(pie_content)):
    explode.append(explodes[i])

print(explode)

plt.title("Programming Chart", fontdict={'size':26})
plt.pie(pie_content, labels=set(label), autopct='%1.1f%%', colors=color, shadow=True, labeldistance=1.1, startangle=140, radius=1.2, explode = (0, 0.1, 0))
plt.axis('equal')
plt.savefig("programming.jpg", dpi=250)
# plt.show()

