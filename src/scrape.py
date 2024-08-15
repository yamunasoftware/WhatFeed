### SCRAPING IMPORTS ###

import processing
import requests
from bs4 import BeautifulSoup

### SCRAPING FUNCTIONS ###

# Scrape Reuters:
def scrape():
  headings = []
  response = requests.get('https://www.bbc.com')

  if '200' in str(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_tags = soup.find_all('h2')

    for h2 in h2_tags:
      headings.append(h2.get_text())
    return headings
  else:
    return None
  
# Run Scraping Steps:
def run_scraping():
  headings = scrape()
  tokenized_headings = processing.delimit(headings)
  processed_headings = processing.filter_news(tokenized_headings, 4)

  combined_sentences = processing.combine_all_tokens(processed_headings)
  final_sentences = processing.clean_sentences(combined_sentences)
  return final_sentences, combined_sentences