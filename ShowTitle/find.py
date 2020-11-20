import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://travel.ettoday.net/category/%E5%8F%B0%E4%B8%AD/", verify=False)
soup = BeautifulSoup(response.text, "html.parser")
link2_tag = soup.find_all(a, "h3")
#link2_tag = soup.find(id='hot-news-index')
#result = soup.find_all("h3", id='hot-news-index', class_="block block_z1 xfb", limit=5)
#print(result)
print(link2_tag)
