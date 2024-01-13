import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import html5lib
import spacy
import re
sentence=input("search:-")
nlp = spacy.blank('en')
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edge/12.246"}
def extract_keywords_spacy(sentence):
    doc = nlp(sentence.lower())
    important_words = [token.text for token in doc if not token.is_stop]
    return important_words
    
keywords_spacy = extract_keywords_spacy(sentence)
print(keywords_spacy)

def path_extraction(url):
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for keyword in keywords_spacy:
            potential_elements = soup.find_all(lambda tag: tag.name.lower() == 'a' and keyword in tag.get_text().lower())
            
            for element in potential_elements:
                href_value = element.get('href')
                return href_value
        return None
    else:
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
        return None
    
webpage=input("website name(https://www.example.com):-")
value=path_extraction(webpage)
print(value)
rr=webpage+value
print(rr)  



def extract_data_from_page(url):
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('body')
        for paragraph in paragraphs:
            print(paragraph.get_text())

    else:
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")

extract_data_from_page(rr)

