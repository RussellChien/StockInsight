# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4, re
from pprint import pprint
import random

# Need to have SSL certificate installed in addition to packages

# Note, Google is tricky, the review rating seem to be formated differently if the browser is Safari or on windows, so only targetting Mac Chrome
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
]

url = 'https://httpbin.org/headers'
user_agent = user_agent_list[random.randint(0, len(user_agent_list)-1)]
headers = {'User-Agent': user_agent}


# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them

text= "site: gartner.com OR g2.com OR getapp.com OR trustradius.com OR capterra.com OR featuredcustomers.com OR softwareadvice.com OR glassdoor.com OR linkedin.com OR abc.com Monday.com rating"
url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url, headers=headers)

soup = bs4.BeautifulSoup(request_result.text)

print(soup.text)

for elem in soup(text=re.compile(r'Rating:')):
	#print('#######\n')
	#print(elem)
	
	print('####### element parent parent ##############\\n')
	#print(elem.parent.parent)

	spans = elem.parent.parent.findChildren("span")
	for span in spans:
		print(span.text)

	#print('####### element parent parent ##############\n')
	

	children = elem.parent.parent.parent.parent.findChildren("div" , recursive=False)
	for child in children:
		#print('----------------- Div ---------------------------\n')
		#print(child)

		if child.attrs.get("data-header-feature") is None:
			print('\n')
			#print(child.attrs.get("data-content-feature"))
		
		else:
			print('----------------- HREF ---------------------------\n')
			print (child.findChildren("div")[0].findChildren("a")[0].get("href"))


		print('--------------------------------------------\n')