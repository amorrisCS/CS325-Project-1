import requests                     # This is a library that allows python to make HTTP requests
from bs4 import BeautifulSoup       # This is a library for parsing HTML and XML
from urllib.parse import urlparse   # This is a library used for extracting path components - mostly used for file naming
import os                           # This is a library used for providing operating system-dependent functionality

def download_and_extract(url):
    try:
        response = requests.get(url)    # Sending GET request to the URL 

        if response.status_code == 200:                             # If GET request successful...
            soup = BeautifulSoup(response.content, 'html.parser')   # Parsing HTML content 
            main_content = soup.find('article')                     # Find and extract the "main content" of the page (main content being information tagged with <article>)

            if main_content:
                filename = urlparse(url).path.replace('/', '_') + '.txt'    # Creating a filename unique to the URL

                with open (filename, 'w', encoding = 'utf-8') as f:
                    f.write(main_content.get_text(separator = '\n'))        # Writing parsed content to file

                print(f"Content extracted from {url} and saved to {filename}.")     # Success
            
            else:
                print(f"No main content found on {url}.")   # Error case
        
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")    # Error case
    
    except Exception as e:
        print(f"An error occured while accessing {url}: {e}")   # Error case

urls_filename = 'URLs.txt'                  # Setting variable to file name that contains the URLs
if os.path.exists(urls_filename):           # Reads URLs from file 
    with open (urls_filename, 'r') as f:
        urls = f.read().splitlines()

        for url in urls:                    # Iteration of URLs
            download_and_extract(url)

else:
    print(f"File '{urls_filename}' not found.")    # Error case
