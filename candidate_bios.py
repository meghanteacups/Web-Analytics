# -*- coding: utf-8 -*-
# Predict 452 Sec 55
# Assignment 1
# Toni Moore

# Original code source - wnds_chapter_3a.py
# from Miller, T. W. (2015). Web and Network Data Science: 
# Modeling Techniques in Predictive Analytics.

# I modified the code for Assignment 1 to extract bios from the 2016 
# U.S. presidential candidates' official web sites using BeautifulSoup
# and write the bios to separate text files.

# -*- coding: utf-8 -*-
# prepare for Python version 3x features and functions
from __future__ import division, print_function

# import packages for web scraping/parsing
import requests  # functions for interacting with web pages
from bs4 import BeautifulSoup  # DOM html manipulation

# test requests package on the home page/about for 2016 U.S. presidential candidates
# obtain the entire HTML text for the page of interest
web_page_About_HC = requests.get('https://www.hillaryclinton.com/about/bio/', auth=('user', 'pass'))
web_page_About_BS = requests.get('https://www.berniesanders.com/about/', auth=('user', 'pass'))
web_page_About_DT = requests.get('https://www.donaldjtrump.com/about/', auth=('user', 'pass'))
web_page_About_TC = requests.get('https://www.tedcruz.org/about/', auth=('user', 'pass'))

# show the status of the page... should be 200 (no error)
web_page_About_HC.status_code
web_page_About_BS.status_code
web_page_About_DT.status_code
web_page_About_TC.status_code

# show the encoding of the page... should be utf8
web_page_About_HC.encoding
web_page_About_BS.encoding
web_page_About_DT.encoding
web_page_About_TC.encoding

# show the text including all of the HTML tags... lots of tags
web_page_About_HC_text = web_page_About_HC.text
print(web_page_About_HC_text)

web_page_About_BS_text = web_page_About_BS.text
print(web_page_About_BS_text)

web_page_About_DT_text = web_page_About_DT.text
print(web_page_About_DT_text)

web_page_About_TC_text = web_page_About_TC.text
print(web_page_About_TC_text)

# -----------------------------------------------------------
# parsing HTML with beautiful soup for Hillary Clinton (HC)
# -----------------------------------------------------------
my_soup = BeautifulSoup(web_page_About_HC_text)
# note that my_soup is a BeautifulSoup object
print(type(my_soup))

# remove JavaScript code from Beautiful Soup page object
# using a comprehension approach
[x.extract() for x in my_soup.find_all('script')] 

# gather all the text from the paragraph tags within the object
# using another list comprehension 
soup_content = [x.text for x in my_soup.find_all('p')]
# show the resulting text string object
print(soup_content)  # note absence of all-blank strings
print(len(soup_content))  
print(type(soup_content))  # a list of character strings

# Write the biography text to a file
f = open('About_HC.txt',"w")
f.write(str(soup_content))
f.close()

# -----------------------------------------------------------
# parsing HTML with beautiful soup for Bernie Sanders (BS)
# -----------------------------------------------------------
my_soup = BeautifulSoup(web_page_About_BS_text)
# note that my_soup is a BeautifulSoup object
print(type(my_soup))

# remove JavaScript code from Beautiful Soup page object
# using a comprehension approach
[x.extract() for x in my_soup.find_all('script')] 

# gather all the text from the paragraph tags within the object
# using another list comprehension 
soup_content = [x.text for x in my_soup.find_all('p')]
# show the resulting text string object
print(soup_content)  # note absence of all-blank strings
print(len(soup_content))  
print(type(soup_content))  # a list of character strings

# Write the biography text to a file
f = open('About_BS.txt',"w")
f.write(str(soup_content))
f.close()

# -----------------------------------------------------------
# parsing HTML with beautiful soup for Donald Trump (DT)
# -----------------------------------------------------------
my_soup = BeautifulSoup(web_page_About_DT_text)
# note that my_soup is a BeautifulSoup object
print(type(my_soup))

# remove JavaScript code from Beautiful Soup page object
# using a comprehension approach
[x.extract() for x in my_soup.find_all('script')] 

# gather all the text from the paragraph tags within the object
# using another list comprehension 
soup_content = [x.text for x in my_soup.find_all('p')]
# show the resulting text string object
print(soup_content)  # note absence of all-blank strings
print(len(soup_content))  
print(type(soup_content))  # a list of character strings

# Write the biography text to a file
f = open('About_DT.txt',"w")
f.write(str(soup_content))
f.close()

# -----------------------------------------------------------
# parsing HTML with beautiful soup for Ted Cruz (TC)
# -----------------------------------------------------------
my_soup = BeautifulSoup(web_page_About_TC_text)
# note that my_soup is a BeautifulSoup object
print(type(my_soup))

# remove JavaScript code from Beautiful Soup page object
# using a comprehension approach
[x.extract() for x in my_soup.find_all('script')] 

# gather all the text from the paragraph tags within the object
# using another list comprehension 
soup_content = [x.text for x in my_soup.find_all('p')]
# show the resulting text string object
print(soup_content)  # note absence of all-blank strings
print(len(soup_content))  
print(type(soup_content))  # a list of character strings

# Write the biography text to a file
f = open('About_TC.txt',"w")
f.write(str(soup_content))
f.close()
