import requests
from bs4 import BeautifulSoup
import json
import os

#test = open("spider/test.txt","w",encoding='UTF-8')


def program(returnurl,s):
	print("---printing page"+str(s+1)+"----")
	r = requests.get(returnurl) #將網頁資料GET下來
	soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

	q = 1
	p = 1
	links = []
	for i in range(1,4):
		urllist = soup.findAll("li",class_="loop-"+ str(i))
		# print (urllist)
		for j in urllist:
			titleurl=j.find("h2",{"class":"entry-title"}).find("a").get("href")
			print(titleurl)
			links.append(titleurl)
	for x in links:
		os.makedirs(#make file for the images)  
		print ("post"+str(p))
		r = requests.get(x)
		soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
		imglist = soup.find_all("img",class_= "pict")

		for k in imglist:
			pic=requests.get("https:"+k["src"])
			img2=pic.content
			pic_out=open(#were you save your file,"wb")
			pic_out.write(img2)
			pic_out.close()
			q+=1
		p+=1
	
	r = requests.get(returnurl) #將網頁資料GET下來
	soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
	urllist = soup.findAll("div",class_="nav-links")
	# print (urllist)
	for x in urllist:
		url = x.find("a",class_="next page-numbers").get("href")
		print(url)
	
	program(url,s+1)


program(#your link here) 
