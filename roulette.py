import xml.etree.ElementTree
import os
import feedparser
import datetime


link = feedparser.parse("https://www.stxavier.org/calendar/calendar_27.rss")
a = ""
temp = 0
ks = []
for i, post  in enumerate(link.entries):
    a += (post.title + " " + post.description)
    b = a.replace("<br>", "\n").replace("<p>", "").replace("</p>", " ").replace("<br />", " ")
    ks.append(i)
daylist = b.split("\t\t\t\t")
current_day = datetime.datetime.now()

print(daylist[ks[0]])
    
    