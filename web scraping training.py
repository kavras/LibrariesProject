import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
s = BeautifulSoup(url_txt, "html.parser")
print(s.prettify())
print(s.title) ###with html tag##
print(s.title.string) ##shown as a string##

tag = s.find_all('a')
print(tag)

tables = s.find_all('table')
print(tables)

my_table = s.find('table', class_='wikitable sortable plainrowheaders')
table_links=my_table.find_all('a')
print(table_links)

actors = []
for links in table_links:
    actors.append(links.get('title'))
print(actors)