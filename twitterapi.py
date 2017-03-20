
from twitter import *

OAUTH_TOKEN = '815942734485848064-o3CgIHcdkKK6cGqnwClQt50n9ix6FuV'
OAUTH_SECRET = '3uGnwiQDycO34GORI9w82Si8IDMoJDNVQIn6M9J6GBYvZ'

CONSUMER_KEY = 'weF00H9WatIqAFf9wN0MsXZGo'
CONSUMER_SECRET = '23DH0yPB4v7fHErNsZyVWlMxeTIdeWMIX3otLNwoXkt2obiJyl'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#t.statuses.update(status="TWEET DESDE API")
x = t.statuses.home_timeline(count=2)
print (x)
