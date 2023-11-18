import requests
from bs4 import BeautifulSoup

link = "https://www.w3schools.com/python/"
response = requests.get(link).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div',class_='w3-panel w3-info intro')

learn_python = block.find_all('h2')
python_text_1 = block.find_all('p')
print(learn_python[0].text)
for i in python_text_1:
    print(i.text)


