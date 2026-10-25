import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url, timeout=15)

print("Status code:", response.status_code)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.find("title")

if page_title is not None:
  print("Page title:", page_title.get_text(strip=True))
else:
 print("Page title not found.")
