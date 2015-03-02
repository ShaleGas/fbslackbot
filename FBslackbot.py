import requests #Beacuse Python http is just too broken
import json		#Facebook formats all its graph API response data in JAY-SON!

################
#Facebook stuff#
################

#Facebook User ID or group ID/Page ID
uid = '226864370853850' 		

#field variable change to query for different shit
fvar = "feed.limit(10)" 	

#Facebook access token with read permission to Hacksoc group
access_token = ''

#Graph API format get request
r = requests.get("https://graph.facebook.com/" + uid + "?fields=" + fvar + "&access_token=" + access_token)

#JSON format response 
print r.json()['feed']['data'][1]['created_time']

#For loop iterates through number of posts found in feed (restricted by feed.limit(x)) prints created time
#Planning to use created time to track what posts have already been forwared to the webhook 
for x in range(len(r.json()['feed']['data'])):
	print r.json()['feed']['data'][x]['created_time']
	
##This section is mainly prints for debuging and feeling around the nested JSON
postid = r.json()['feed']['data'][0]['id']
fvar2 = 'created_time'
cr = requests.get("https://graph.facebook.com/" + postid + "?fields=" + fvar2 + "&access_token=" + access_token)
print cr.json()['created_time'] 

print r.url

#############
#Slack stuff#
#############

#Webhook address
whaddr = "" 

#Payload (JSON)
payload='{"text": "happy now?", "channel": "#general", "username": "police-bot", "icon_emoji": ":cop:"}'

#POST to webhook, data(JSON)
#p = requests.post(whaddr, data=payload) #POST request 

#debug print line to check request formed correctly
#print p.text


# Sample of slack POST request suing curl
# curl -X POST --data-urlencode 'payload={"text": "This is posted to <#general> and comes from *monkey-bot*.", "channel": "#general", "username": "monkey-bot", "icon_emoji": ":monkey_face:"}' https://hooks.slack.com/services/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
