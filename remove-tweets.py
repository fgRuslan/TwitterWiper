from twitter import *

config = {}
execfile("config.py", config)

user = raw_input("Type your user name here:")

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
results = twitter.statuses.user_timeline(screen_name = user)

print "Removing your tweets, this may take a while..."

for status in results:
	remove_results = twitter.statuses.destroy(id = status["id"])
