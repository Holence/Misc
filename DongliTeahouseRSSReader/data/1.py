from DTPySide.DTFunction import *

import feedparser

# url = 'https://www.youtube.com/channel/UCOP0VkJvcGrR9snmUlPPYMA'
url = 'https://www.w3schools.com/xml/xpath_operators.asp'




def StandardRSS(url):
	feeds=feedparser.parse(url)
	# if feeds.
	Json_Save(feeds,"2.json")
	# 	if "title" in feeds.feed and feeds.entries!=[]:
	# 		return ("Done",feeds.feed.title,feeds.entries)
	# 	else:
	# 		return ("Invalid",None,None)
	# except:
	# 	return ("Failed",None,None)
StandardRSS("https://www.eva-all.com/news/feed/")