

##############################################################################################
# Examples showing basics of NLP
#
# Usage:
#	python3 nlp_test.py
#
# Installation:
#	python3
#	user_nltk_dir = "/home/soumya/nltk_data"
#	nltk.download("book", download_dir=user_nltk_dir)
#
# Adapted from:
# https://github.com/Spaxe/NLTK/blob/contrib/1%20hour%20workshop%20notes.ipynb
#
##############################################################################################

import nltk
import matplotlib
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from nltk.book import *
from nltk.draw.dispersion import dispersion_plot
import re
from nltk import word_tokenize

user_nltk_dir = "/home/soumya/nltk_data"
#nltk.download("book", download_dir=user_nltk_dir)


text4

# How would you calculate the percentage of Text 4 that is taken up by the word "America"?
100.0*text4.count("America")/len(text4)

text2.concordance("monstrous")
text2.similar("monstrous")
text2.common_contexts("monstrous", 2)
text2.common_contexts(["monstrous", "very"])

text2.collocations()
dispersion_plot(text1, ["whale"])

dispersion_plot(text4, ["citizens", "democracy", "freedom", "duties", "America"]) # plot five words longitudinally
text4.similar("citizens")
text4.concordance("citizen")


url = "http://en.wikipedia.org/wiki/Smog"
raw = urlopen(url).read()
print(type(raw))
print(raw[100:200])

soup = BeautifulSoup(raw, 'html.parser')
print(type(soup))

#Find all the paragraphs, and put them into a list
texts = []
for para in soup.find_all('p'):
    text = para.text
    texts.append(text)

print(texts[:10])

regex = re.compile('\[[0-9]*\]')
joined_texts = '\n'.join(texts)
joined_texts = re.sub(regex, '', joined_texts)
print(type(joined_texts))
print(joined_texts[:100])

wordlist = nltk.word_tokenize(joined_texts)
wordlist[:8]

#For some other types of analysis, we'll need to create an NLTK text object
good_text = nltk.Text(wordlist)
good_text.concordance('smog')
good_text.common_contexts(['smog', 'pollution'])

#NLTK_file = open("NLTK-Smog.txt", "w", encoding='UTF-8')
#NLTK_file.write(str(wordlist))
#NLTK_file.close()


#speech = open('../corpora/fraser-year/1975/UDS2013680-678-full.txt', "r").read()
#tokens = word_tokenize(speech)
#print(tokens[:100])
