import urllib.request as req
# import requests as req
from bs4 import BeautifulSoup

class Scraper:

	def __init__(self, url):
		self.url = url

	def scrape(self):
		r = req.urlopen(self.url) # returns and store a response object
		html = r.read() # get the html of url
		parser = "html.parser"
		sp = BeautifulSoup(html, parser) # parse html
		
		for tag in sp.find_all("a"): # return "a" tags
			url = tag.get("href") # from the tag, get link/url
			print(f"\n{url}")

scrape = Scraper("https://news.google.com")
scrape.scrape()