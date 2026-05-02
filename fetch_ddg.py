import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
         with urllib.request.urlopen(req) as response:
             html = response.read()
             soup = BeautifulSoup(html, 'html.parser')
             results = soup.find_all('a', class_='result__snippet')
             for r in results[:5]:
                 print(r.get_text())
    except Exception as e:
         print(f"Error: {e}")

print("--- DDG Search: Darktable scene-referred workflow features ---")
search_ddg("Darktable scene-referred workflow features")
print("\n--- DDG Search: intelligent cropping AI photo editing behavior ---")
search_ddg("intelligent cropping AI photo editing behavior table stakes differentiators")
print("\n--- DDG Search: Darktable diffuse or sharpen deblur noise reduction best practices ---")
search_ddg("Darktable diffuse or sharpen deblur noise reduction best practices")
