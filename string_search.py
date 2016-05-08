from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import csv
import json
import requests
import urllib

#todo change lines to be a global constant and one time load
def find_string(string):
	with open('ratio.txt') as f:
		lines = f.read().splitlines()
	ratio = process.extractOne(string, lines)[0]
	with open('companies.txt') as f:
		lines = f.read().splitlines()
	company = process.extractOne(string, lines)[0]
	return ratio + " " + company

###method to take string and ask data from screener.in
def get_screener_data(company,ratio):
    company_dictionary = {}
    with open('company_data.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            company_dictionary[row[0]] = row[1]
    company_bse_name = company_dictionary[company]
    url = "https://www.screener.in/api/company/" + company_bse_name
    r = requests.get(url)
    company_id = r.json()["warehouse_set"]["id"]
    query = {"q": ratio}
    #todo write method to update this from cache or Ram
    cookie = {'sessionid': 'gqnbs0gobw18pzykfyawuhned3pwqy5r'}
    url  =  "https://www.screener.in/api/company/" + str(company_id) + "/ratio/?" + urllib.urlencode(query)
    r = requests.get(url, cookies=cookie)
    return r.json()["ratio"][1]
