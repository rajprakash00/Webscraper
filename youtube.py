#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
from pytube import YouTube
import requests

URL="https://www.youtube.com"
URL2="/results?search_query="
query ="lose+yourself"              #my favourite video and song
r = requests.get(URL+URL2+query)
soup=bs(r.text,'html.parser')
vid=soup.findAll('a',attrs={'class':'yt-simple-endpoint'}) #it varies for different PCs
vidlist=[]
for v in vid:
	temp=URL + v['href']
	vidlist.append(temp)

##main scraping process starts

count=0
for item in vidlist:
	count+=1
	yt=YouTube(item)
	#video=yt.streams.first(file_extension='mp4')   #you can do this also insted of .get()   
	video=yt.get('mp4','360p')
	print(yt.set_filename('Video_'+str(count)))
	video.download('path of folder to download')





