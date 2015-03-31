#from flask import Flask
#from flask import render_template
#from flask import request

#import tweepy

#app = Flask(__name__)
CONSUMER_TOKEN = "EDVg9TMu7r4FKZbIFtmO0eMqn"
CONSUMER_SECRET="H2P7e7AF0px7pYbelTSn898lbtakeUTGIIo3ct05Cs8gjzS5kM"
CALLBACK_URL = 'http://localhost:5000/verify'



#app.config.from_object(__name__)


#auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, secure=True)
#auth.set_access_token(TOKEN, TOKEN_KEY)

#api=tweepy.API(auth)

#@app.route("/tweets")
#def show_tweets():
#	print api.user_timeline()

#if __name__ == "__main__":
#	app.run(host="0.0.0.0", port=5000,debug=True)

from flask import Flask
from flask import request
import flask 
import tweepy
app = Flask(__name__)

#config
	
#session = dict()
#db = dict() #you can save these values to a database

@app.route("/tweets")
def get_tweets():
	auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET, CALLBACK_URL)
	#auth.access_token.key="3130263688-8u8afiIquiohkTJHhWXcXHjEx7tLXsbCDlVkyP8"
	#auth.access_token.secret="73BAHWDREId3kdLvUwBk4LLgtdpDxn1UfjrFds8EBprtf"
	auth.set_access_token('3130263688-8u8afiIquiohkTJHhWXcXHjEx7tLXsbCDlVkyP8', '73BAHWDREId3kdLvUwBk4LLgtdpDxn1UfjrFds8EBprtf')
	api = tweepy.API(auth)
	return flask.render_template('tweets.html', tweets=api.user_timeline())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000,debug=True)