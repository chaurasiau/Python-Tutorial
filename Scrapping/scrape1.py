# import libraries
import urllib3
from bs4 import BeautifulSoup

# specify the url
url = "http://www.bloomberg.com/quote/SPX:IND"

# query the website and return the html to the variable ‘page’
http = urllib3.PoolManager()

response = http.request('GET', url)
soup = BeautifulSoup(response.data)

# ---------------------------------------------------------
# Another way to do the same thing
# import requests
# url = "url"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# ---------------------------------------------------------

name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print(f'name = {name}')
