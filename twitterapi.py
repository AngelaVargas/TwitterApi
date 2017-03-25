
from twitter import *
import tweepy

TOKEN_ACCESS = '815942734485848064-o3CgIHcdkKK6cGqnwClQt50n9ix6FuV'
TOKEN_SECRET = '3uGnwiQDycO34GORI9w82Si8IDMoJDNVQIn6M9J6GBYvZ'

CONSUMER_KEY = 'weF00H9WatIqAFf9wN0MsXZGo'
CONSUMER_SECRET = '23DH0yPB4v7fHErNsZyVWlMxeTIdeWMIX3otLNwoXkt2obiJyl'


#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN_ACCESS, TOKEN_SECRET)

x = tweepy.API(auth)


#update_status es para actualizar nuestro estado, es decir, escribir un tweet
#x.update_status('Funciona!')

#Para mostrar los últimos tweets escritos por TI
for tweets in x.user_timeline():
   print(tweets.created_at)			#Te escribe la fecha en la que el tweet se escribió
   print(tweets.text)					#Te escribe el texto del tweet
   print(' -'*20)						#Para separar un tweet de otro 


#Para mostrar los últimos tweets escritos por los USUARIOS QUE SIGUES, en este caso sólo los dos últimos
for tweets in x.home_timeline(count=1):
    print(tweets.created_at)
    print(tweets.user.screen_name)		#Te escribe el usuario que lo escribió
    print(tweets.text)
    print(' *'*40)

#Para buscar contenido que lleve la palabra q='word'
for tweets in x.search(q='Ghost',count=1, result_type='recent'):	#Con result_type='recent' conseguimos resultados recientes en la búsqueda
    print(tweets.created_at)
    print(tweets.user.screen_name)
    print(tweets.text)
    print(' @'*40)


#Con la función get_user obtienes toda la información de un usuario de twitter

user = x.get_user('DisneySpain')
#print(user)

name = user.screen_name			#Nombre público

followers = user.followers_count			#Obtienes el número de seguidores
print("Followers of " + str(name) + ": " + str(followers))


retweets = user.status.retweet_count				#Obtienes el número de retweets
print("Retweets of " + str(name) + ": " + str(retweets))

favorites = user.status.favorite_count
print("Favorites of " + str(name) + ": " + str(favorites))




