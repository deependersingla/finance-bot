from fuzzywuzzy import process
from fuzzywuzzy import fuzz

#todo change lines to be a global constant and one time load
def find_string(string):
	with open('whitelabelled_words.txt') as f:
		lines = f.read().splitlines()
	return process.extractOne(string, lines)[0]