from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.cpubenchmark.net/cpu.php?cpu=AMD+Ryzen+5+5600X&id=3859').text
print(html_text)