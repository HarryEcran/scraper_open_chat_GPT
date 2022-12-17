import requests
from bs4 import BeautifulSoup
import re

fh = open("output.txt", "a")
#fh.write("test \n test test")
#fh.write("yes plse")

#URL = "https://www.answers.com/guide/41472"

for n in range(3754,60000):
    print(str(n))

    try:
        URL = "https://www.answers.com/guide/" + str(n)

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        if (page.status_code == 404):
            continue
    except:
        continue

    else:
        try:
            rating = soup.find(class_="caption2 font-bold mr-2").text
            reviews = soup.find(class_="caption2 ml-1").text
            m = re.search('^\d+', reviews)
            reviews = m.group(0)
        except:
            rating = "0"
            reviews = "0"

        try:
            subject = soup.find(class_="flex h-full w-auto overflow-x-scroll no-scrollbar").text
            questions = soup.find_all(class_="caption3 leading-4.5 pr-2 col-span-1")
            questions = [x.text.replace("\n", " ") for x in questions]
            answers = soup.find_all(class_="border-l border-solid border-primaryLight pl-2 col-span-2 caption1 noMargin leading-4.5 allPrimaryColor")
            answers = [x.text.replace("\n", " ") for x in answers]

            for i in range(0,len(questions)):
                fh.write(str(n) + "_" + str(i) + "\t" + str(questions[i]) + "\t" + str(answers[i]) + "\t" + str(rating) + "\t" + str(reviews) + "\t" + str(subject) + "\n")

        except:
            continue

        

fh.close()