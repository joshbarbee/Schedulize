import xml.etree.ElementTree
import os
import feedparser
import datetime


link = feedparser.parse("https://www.stxavier.org/calendar/calendar_27.rss")
a = ""
temp = 0
for post in link.entries:
    a += (post.title + " " + post.description)
    b = a.replace("<br>", "\n").replace("<p>", "").replace("</p>", " ").replace("<br />", " ")

daylist = b.split("\t\t\t\t")
current_day = datetime.datetime.now()

print(daylist[current_day.day])
    
    