import requests
from bs4 import BeautifulSoup
import json


def simple_dt_scraper(url):
    print(f"--- Scanning: {url} ---")
    try:

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, timeout=10, headers=headers)


        soup = BeautifulSoup(response.text, 'html.parser')


        text_content = soup.get_text().lower()


        keywords = ['probiotic', 'strain', 'gut', 'cfu', 'clinical', 'health']
        found_signals = [word for word in keywords if word in text_content]

        record = {
            "company_name": soup.title.string.strip() if soup.title else "Unknown",
            "url": url,
            "detected_signals": found_signals,
            "status": "Success"
        }
        return json.dumps(record, indent=4)

    except Exception as e:
        return json.dumps({"status": "Error", "message": "Site blocked or unavailable"})

print(simple_dt_scraper("https://www.probi.com/"))