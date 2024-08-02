import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all 'a' tags (which define hyperlinks)
        links = soup.find_all('a')
        
        # Extract and return the href attribute from each link
        return [link.get('href') for link in links if link.get('href')]
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

# Example usage
url = "https://chicasentecrd-proyectos.github.io/main-site/twenty-four.html"  # Replace with the website you want to scrape
links = scrape_links(url)

# Print the links
for link in links:
    print("https://chicasentecrd-proyectos.github.io/main-site/" + link)