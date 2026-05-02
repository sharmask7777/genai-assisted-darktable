import urllib.request
from bs4 import BeautifulSoup
import json

urls = [
    "https://docs.darktable.org/usermanual/4.6/en/module-reference/processing-modules/diffuse/",
    "https://docs.darktable.org/usermanual/4.6/en/overview/workflow/edit-scene-referred/"
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
         with urllib.request.urlopen(req) as response:
             html = response.read()
             soup = BeautifulSoup(html, 'html.parser')
             text = soup.get_text(separator='\n', strip=True)
             print(f"--- Content from {url} ---")
             print(text[:4000]) 
    except Exception as e:
         print(f"Error fetching {url}: {e}")
