import requests
from bs4 import BeautifulSoup

with requests.Session() as c:
	url = 'https://www.superliquor.co.nz/beer-cider/'
	DAY = '01'
	MONTH = '01'
	YEAR = '1980'
	c.get(url)

	login_data = dict(dob_dd = DAY, dob_mm = MONTH, dob_yyyy=YEAR)

	c.post(url, data=login_data)

	page = c.get("https://www.superliquor.co.nz/beer-cider/")
	soup = BeautifulSoup(page.content, "html.parser")


	for product in soup.findAll(class_="product_name"):
		 
		 print product.findAll("h4")

	for price in soup.findAll(class_="price btn btn-danger"):
		print price


