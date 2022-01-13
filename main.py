"""
PROJECT: Web_Crawler
Aurthor: CHIDERA C. ONWURAH

"""
#IMPORTS

import json
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError,RequestException,Timeout

class Scrape:
	# initialise 
	def __init__(self,*args):
		self.banner = ("\t\t<<<  WEB SCRAPER for https://mavin.io >>>\n")
		self.response = ("[ INFO ] Successfully scraped data from website")
		self.num = 	("2956") 	# modified when scraping another [ item_number ]...
		self.file = ("log"+ self.num +".csv")
	def	save_data(self,itemname,itemprice,picture,itemdate_sold,itemshipping_cost):
		#filter the strings
		name = str(itemname).replace(",","")
		name = name.replace(";","")
		name = name.replace("'"," ")
		name = name.replace('"'," ")
		price = str(itemprice).replace(",","")
		price = price.replace(";","")
		image = str(picture).replace(",","")
		image = image.replace(";","")
		date_sold = str(itemdate_sold).replace(",","")
		date_sold = date_sold.replace(";","")
		shipping_cost = str(itemshipping_cost).replace(",","")
		shipping_cost = shipping_cost.replace(";","")
		
		#store in log.csv file
		csv_file = open(self.file,"a",encoding="utf-8")
		raw = ("\n"+name+","+price+","+image+","+date_sold+","+shipping_cost)
		csv_file.write(raw)
		csv_file.close()
	def scrape_data(self,*args):
		print(self.banner)
		page_file = open("log.txt","r")
		page = (page_file.read())
		page_file.close()
		for i in range(int(page), 400000):
			url = ("https://mavin.io/search?q=&amp;bt=sold&amp;cat="+ self.num +"&amp;sort=EndTimeSoonest&amp;page="+str(i))
			print("[ INFO ]: Scraping "+ url + " ...")
			try:
				res = requests.get(url)
				soup = BeautifulSoup(res.content,"html.parser")
				divtags = soup.find_all('div',class_="row result")
				
				page_log = open("log.txt","w")
				page_entry = page_log.write(str(i))
				page_log.close()
				# Loop through
				for tags in divtags:
					name = tags.find("a",class_="modal-link").text
					image = tags.find("img",class_="itemImage")["src"]
					price = tags.find("h3",class_="sold-price").text
					date_sold = tags.find("p",class_="time").text
					shipping_cost = tags.find("h3",class_="sold-price")["data-shipping"]
					self.save_data(name,price,image,date_sold,shipping_cost)
			except ConnectionError or RequestException or Timeout:
				print("[ INFO ]: Network Error ...")
				print("[ INFO ]: Restarting ...")
				break
		print(self.response)
		self.reload()
		
	"""
	There's an easier way to do this but am leaving it as 
	for reasons best known to myself
	
	[ Feel free to alter the codes to yours advantage ]
	"""
	def reload(self):
		page_file = open("log.txt","r")
		page = (page_file.read())
		page = (int(page))
		page_file.close()
		for i in range(page, 400000):
			url = ("https://mavin.io/search?q=&amp;bt=sold&amp;cat="+ self.num +"&amp;sort=EndTimeSoonest&amp;page="+str(i))
			print("[ INFO ]: Scraping again "+ url + " ...")
			try:
				res = requests.get(url)
				soup = BeautifulSoup(res.content,"html.parser")
				divtags = soup.find_all('div',class_="row result")
				page_log = open("log.txt","w")
				page_entry = page_log.write(str(i))
				page_log.close()
				#
				for tags in divtags:
					name = tags.find("a",class_="modal-link").text
					image = tags.find("img",class_="itemImage")["src"]
					price = tags.find("h3",class_="sold-price").text
					date_sold = tags.find("p",class_="time").text
					shipping_cost = tags.find("h3",class_="sold-price")["data-shipping"]
					self.save_data(name,price,image,date_sold,shipping_cost)
			except ConnectionError or RequestException or Timeout:
				print("[ INFO ]: Network Error ...")
				print("[ INFO ]: Restarting ...")
				break
		self.scrape_data()
if __name__ == "__main__":
	main = Scrape()
	main.scrape_data()
	print("[ INFO ] Logs written to csv file")
