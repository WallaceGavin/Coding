#!/usr/bin/env python3

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import pandas as pd

#url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://www.comedymothership.com/shows"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

#print(html)

#href="https://www.showclix.com/event/tim-dillon-headlines-fat-man-kn2k">Sold Out</a></div></div></div></li><li

#class="EventCard_linkButton__9_Cv3 disabled clickable button" href="https://www.showclix.com/event/tim-dillon-headlines-fat-man-fgggu">Sold Out</a></div></div></div></li><li style="opacity:0"><div 

#class="EventCard_textWrapper__0ckCQ"><div class="EventCard_titleWrapper__8GSjU EventCard_eventInfo__oo_VE"><div class="h6">Thursday, Oct 31</div><h3>Brian Holtzman and Friends</h3></div><ul 

#bring in soup
soup = BeautifulSoup(html, "html.parser")

#create an empty list for events
events = []

#extract all event cards from the HTML
event_cards = soup.find_all("div", class_="EventCard_textWrapper__0ckCQ")

for card in event_cards:
	# Extract date (if available)
	date = card.find("div", class_="h6").get_text(strip=True) if card.find("div", class_="h6") else "N/A"
	
	# Extract title (if available)
	title = card.find("h3").get_text(strip=True) if card.find("h3") else "N/A"
	
	# Check if the event is sold out by looking for "Sold Out" in following <a> tag or similar structure
	sold_out = "Available"  # Default to available
	next_sibling = card.find_next_sibling("div")  # Find the next relevant sibling
	if next_sibling:
		sold_out_text = next_sibling.find("a", href=True)
		if sold_out_text and "Sold Out" in sold_out_text.text:
			sold_out = "Sold Out"
			
	# Append the extracted info as a tuple to the events list
	events.append((date, title, sold_out))
	
#the for card in event_cards does not have sold out in that card, need a different ammend loop
	
df = pd.DataFrame(events, columns=["Date", "Title", "Status"])


print(df)

soup.find_all("Sold Out")