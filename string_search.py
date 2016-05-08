from fuzzywuzzy import process
from fuzzywuzzy import fuzz

#todo change lines to be a global constant and one time load
def find_string(string):
	with open('whitelabelled_words.txt') as f:
		lines = f.read().splitlines()
	ratio = process.extractOne(string, lines)[0]
	with open('companies.txt') as f:
		lines = f.read().splitlines()
	company = process.extractOne(string, lines)[0]
	return ratio + " " + company

###method to take string and ask data from screener.in