from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.funda.nl/koop/brunssum/appartement/sorteer-datum-af/').text

soup = BeautifulSoup('html_text','lxml')
objecten_per_dag = soup.find_all('div', class_ = 'search-content-output')
# print( objecten_per_dag)
print( objecten_per_dag)
