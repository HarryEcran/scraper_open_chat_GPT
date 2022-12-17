import requests
from bs4 import BeautifulSoup
import re

fh = open("output_general_questions_question_links.txt", "a")
fh_links = open('output_general_questions_main_links.txt', 'r')
links = fh_links.readlines()

page_count = 1148
start_link = 2

for i in range(start_link,len(links)):
    link = links[i]
    print(i)
    if (re.match("^/", link)):
        questions_left = True
        print(link)
        while questions_left:
            URL = "https://www.answers.com" + link.replace("\n", "") + "?page=" + str(page_count)
            print(URL)
            page_count += 1

            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")

            if (re.search("No questions yet", soup.text)):
                questions_left = False
                print("End of this subject!")
                page_count = 1
                break

            main_subjects = soup.find(class_="bg-white shadow-cardGlow rounded pb-2")
            main_subjects = main_subjects.find_all('a')
            for question_link in main_subjects[1:]:
                check = str(question_link.get('href'))
                if (re.search("\?page=", check) or check == "None"):
                    continue
                else:
                    fh.write(check + "\n")

fh.close()
fh_links.close()