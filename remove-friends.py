from twitter import *
import json

config = {}
execfile("config.py", config)

user = raw_input("Type the user name here:")

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
results = twitter.friends.ids(screen_name = user)

for n in range(0, len(results["ids"]), 100):
	ids = results["ids"][n:n+100]
print(ids)
for i in range(0,len(ids)):
    results = twitter.friendships.destroy(user_id = ids[i])
