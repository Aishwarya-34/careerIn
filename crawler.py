import requests 
from urllib.parse import urlparse
import json
from flask import Flask
from flask import request
from bs4 import BeautifulSoup
import html5lib

app = Flask(__name__)

s = requests.Session()

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content

@app.route('/', methods=['POST', 'GET'])
def industrySearch():
	if request.method == 'POST':
		if valid_industry(request.args['industry']):
			return query_industry(request.args['industry'])
		else:
			return 'Invalid industry'
	else:
		return "CareerIn Server"

def industry_to_string(industry):
	industry = [letter.lower() for letter in industry]
	industry = ''.join(industry)
	industry = industry.replace(" ", "+")
	return industry

def valid_industry(industry):
	industry = industry_to_string(industry)
	URL = "https://www.indeed.com/jobs?q=" + industry + "&l="
	isValid_soup = BeautifulSoup(fetch(URL), 'html5lib')
	invalid = isValid_soup.findAll('div', attrs={'class':'bad_query'})
	if (invalid != []):
		return True

	return True

def query_industry(industry):
	# make input industry lowercase string separated by "+" instead of " "
	try:
		industry = industry_to_string(industry)
		internships = []
		paginator = 0
		while(paginator < 10):
			URL = "https://www.indeed.com/jobs?q=" + industry + "&jt=internship&start=" + str(paginator)
			print("URL :",URL)
			list_soup = BeautifulSoup(fetch(URL), 'html5lib')
			jobs = list_soup.findAll('div', attrs={'class':'job_seen_beacon'})
			for job in jobs: 
				title = job.findAll('h2', attrs={'class':'jobTitle'})[0].findAll('span')[0].get('title')
				company = job.findAll('span', attrs={'class':'companyName'})
				if company == None:
					company=""
				else:
					company = company[0].findAll('a')[0].contents[0]
				print("Company :",company)

				associate_link = job.findAll('td', attrs={'class':'resultContent'})
				print(associate_link)
				link = "https://www.indeed.com" 
				if associate_link ==None or len(associate_link) ==0:
					link = URL
				else:
					associate_link = associate_link[0].findAll('a')[0].get('href')
					link = link+associate_link
				print("Link :",link)
				body = ""
				# if(associate_link !=None or len(associate_link) !=0):
				# 	job_soup = BeautifulSoup(fetch(link), 'html5lib')
				# 	strings = job_soup.findAll('div', attrs={'class':'jobsearch-jobDescriptionText'})
				# 	if strings !=None or len(strings) !=0:
				# 		strings = strings[0].stripped_strings
				# 		for string in strings:
				# 			body = body + string.strip()

				internships.append({
					"title": title,
					"company": company,
					"link": link,
				})

			paginator = paginator + 10
	except:
		print("Some Scrap error")
	

	return {"Response":"good",
	"Internship": internships}

app.run(debug = True)