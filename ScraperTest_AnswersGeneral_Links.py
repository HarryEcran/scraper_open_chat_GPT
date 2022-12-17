import requests
from bs4 import BeautifulSoup
import re

fh = open("output_general_questions_main_links.txt", "a")

URL = "https://www.answers.com/subjects"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

main_subjects = soup.find(class_="bg-white md:rounded shadow-cardGlow mt-4 p-4")
main_subjects = main_subjects.find_all('a')
main_links = []
for link in main_subjects:
    main_links.append(link.get('href'))

URL = "https://www.answers.com"

for link in main_links:
    URL = "https://www.answers.com" + link

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    sub_subjects = soup.find(class_="bg-white md:rounded shadow-cardGlow mt-4 p-4")
    sub_subjects = sub_subjects.find_all('a')
    sub_links = []
    for link in sub_subjects:
        sub_links.append(link.get('href'))

    for link in sub_links:
        fh.write(str(link) + "\n")

    

fh.close()