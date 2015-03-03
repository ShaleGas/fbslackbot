import requests #Beacuse Python http is just too broken
import json		#Facebook formats all its graph API response data in JAY-SON!
from collections import OrderedDict

################
#Facebook stuff#
################

#Facebook User ID or group ID/Page ID
uid = '' 		

#field variable: change to query for different shit and or amount of shit
#the feed.limit(number) seems to refer to pagination rather than posts.
fvar = "feed.limit(2)" 	

#Facebook access token with read permission to Hacksoc group
access_token = ''

#Graph API format get request
r = requests.get("https://graph.facebook.com/" + uid + "?fields=" + fvar + "&access_token=" + access_token)

#Var for number of posts in feed 
NumPosts = len(r.json()['feed']['data'])

#Some kind of system to track what posts have been posted, what posts
#are new, all that stuff need implemented here...
#Last Scraped Date
#LastScrape = ''


#The Slack function hanlding the webhook, formating, etc. 
def slackpost(name, message):

	#Webhook address
	whaddr = "https://hooks.slack.com/services/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" 

	#All the standard message vars
	text = message 
	channel = '#general'
	username = 'facebook'
	emoji = ':cop:'

	#All the attachment vars
	fallback = ""
	color = ""
	pretext = "" 
	author_name = name
	author_link = ""
	author_icon = ""
	title = ""
	title_link = ""
	attachtext = message
	image_url = ""

	#Full payload including attachement //This may work with a stannard dictionary,
	#I thought the order may have been an issue when debugging the JSON -seems to work anyway 
	payload = OrderedDict([( 'text',text),
						   ('channel',channel),
						   ('username',username), 
						   ('icon_emoji',emoji),
						   ('attachments', [{"fallback":fallback,
						   					 "color":color,
						   					 "pretext":pretext,
						   					 "author_name":name,
						   					 "author_link":author_link,
						   					 "author_icon": author_icon,
						   					 "title": title,
						   					 "title_link": title_link,
						   					 "text": attachtext,
						   					 "image_url": image_url}])])

	#Dictionary to JSON for POST
	jsonpayload = json.dumps(payload)
	
	#Needed to pass this to another var, 
	#Probably some type issue here, passing it to antoher variable fixes it. 
	anotherjsonpayload = jsonpayload 

	#POST to webhook, data(JSON)
	p = requests.post(whaddr, data=anotherjsonpayload)

	#debug print line to check request formed correctly
	print p.text

#For loop iterates through number of posts found in feed (restricted by feed.limit(x))
#Planning to use created time to track what posts have already been forwared to the webhook 
#Riddled with prints for debugging

for x in range(NumPosts):
	#print r.json()['feed']['data'][x]['created_time']
	date = r.json()['feed']['data'][x]['created_time']
	#print r.json()['feed']['data'][x]['from']['name'].encode('utf-8') 
	name = r.json()['feed']['data'][x]['from']['name'].encode('utf-8')
	print name
	
	#Not all feed posts are the same or conform to the same JSON structure
	#This try/catch will probably need significant expansion but has worked
	#with my use case so far. 
	try:
		print r.json()['feed']['data'][x]['message']
		message = r.json()['feed']['data'][x]['message']
	except KeyError:
		print r.json()['feed']['data'][x]['story']
		message = r.json()['feed']['data'][x]['story']
	
	#Debug prints; break after each 'post', url so that I could check some stuff
	#in the browser
	
	print 'BREAK'
	print r.url
	
	#The slackpost function handles the webhook to Slack, can be expanded for 
	#alot more vars
	slackpost(name, message)

#Print URL for debugging 
print r.url


