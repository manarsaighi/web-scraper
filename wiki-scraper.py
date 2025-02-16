# send http requests
import requests
# Beautiful Soup is a Python library that makes it easy to scrape 
# information from web pages. It sits atop an HTML or XML parser and 
# provides Pythonic idioms for iterating, searching, and modifying the 
# parse tree.
from bs4 import BeautifulSoup


# Ask the user for a Wikipedia topic and format it correctly
# strip to remove extra spaces before or after input
# title to capitalise the first letter of each word
topic = input("Enter a Wikipedia topic: ").strip().title()

# topic replace to chance spaces to underscores (wikipedia urls separate words this way)
url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"

# Fetch the Wikipedia page
# sending a GET request
response = requests.get(url)

# status code of 200 means OK
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Check if Wikipedia returned a "not found" page
    if soup.find("table", class_="noarticletext"):
        print("\n❌ Wikipedia page not found. Check the spelling or try a different topic.")
    else:
        # Find all paragraphs in the main content
        paragraphs = soup.find("div", class_="mw-parser-output").find_all("p")

        # Get the first non-empty paragraph
        summary = next((p.text.strip() for p in paragraphs if p.text.strip()), None)

        if summary:
            print("\n🔹 Wikipedia Summary:\n", summary)
        else:
            print("\n⚠️ No meaningful summary found on this page.")

else:
    print("\n❌ Failed to retrieve the page. Check your internet connection.")
