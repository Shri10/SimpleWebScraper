# Simple Web Scraper

A Python script that scrapes all tags and their content from a given webpage and saves the data in a CSV file.

Use this to get the data, After which analyse what exactly you want to scrape.

Author: Shriraj PETHE.

## Features

- Fetches the webpage content from a user-provided URL
- Parses the HTML content and extracts all tags, text, classes, ids etc.
- Saves data in a CSV file with a unique timestamped filename

## Prerequisites

- Python 3.x
- BeautifulSoup4
- Requests

## Installation

1. Clone the repository or download the `scrape_all_tags_v2.py` script file.

2. Install the required Python packages:

```bash
pip install beautifulsoup4 requests
```

## Usage

1. Run the script:

```bash
python scrape_all_tags_v2.py
```

2. Enter the URL when prompted.

3. The script will fetch the webpage, parse the HTML content, find all the tags, and save the data in a CSV file in the same directory as the script.

## License

This project is licensed under the MIT License. See the LICENSE file for details (if applicable).