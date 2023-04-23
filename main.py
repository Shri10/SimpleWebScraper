import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from urllib.parse import urljoin

def extract_attributes(tag):
    attributes = {}
    for attr, value in tag.attrs.items():
        attributes[attr] = ' '.join(value) if isinstance(value, list) else value
    return attributes

# Prompt the user for a URL
url = input("Enter the URL: ")

# Fetch the webpage
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all tags
found_tags = soup.find_all()

# Generate a unique filename with the current date and time
now = datetime.now()
filename = f'scraped_data_{now.strftime("%Y%m%d_%H%M%S")}.csv'

# Save the data to a CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Tag', 'Text', 'Attributes', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for tag in found_tags:
        text_content = tag.get_text(strip=True)
        attributes = extract_attributes(tag)

        # Check if the tag has a 'href' attribute
        relative_link = tag.get('href', None)
        if relative_link:
            link = urljoin(url, relative_link)
        else:
            link = ''

        writer.writerow({'Tag': tag.name, 'Text': text_content, 'Attributes': attributes, 'URL': link})

print(f"Data saved to {filename}")
