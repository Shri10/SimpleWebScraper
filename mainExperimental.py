import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

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
    fieldnames = ['Tag', 'Class', 'ID', 'Text', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for tag in found_tags:
        text_content = tag.get_text(strip=True)

        # Extract class and ID information
        class_names = ' '.join(tag['class']) if tag.has_attr('class') else ''
        tag_id = tag['id'] if tag.has_attr('id') else ''

        # Check if the tag has a 'href' attribute
        link = tag.get('href', '')

        writer.writerow({'Tag': tag.name, 'Class': class_names, 'ID': tag_id, 'Text': text_content, 'URL': link})

print(f"Data saved to {filename}")
