import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://example.com"

# Send request to website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract all headings
for heading in soup.find_all("h1"):
    print(heading.text)