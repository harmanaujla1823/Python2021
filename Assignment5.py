import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/dna"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
print(soup.prettify())

print("----TITLE-----")
print(soup.title.text)


print("----Div Tags-----")

divTags = soup.find_all("div", class_="js-tweet-text-container")
for tag in divTags:
    # print(tag)
    print(tag.text)
    print("^^^^^^^^^^^")