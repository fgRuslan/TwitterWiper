from twitter import *
import json

config = {}
try:
        exec(compile(open("config.py").read(), "config.py", 'exec'), config)
except IOError:
        print()
        print("Error: No configuration file found. Creating a new one...")
        exec(compile(open("auth.py").read(), "auth.py", 'exec'))
        exit(1)

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
results = twitter.friends.ids()#screen_name = user
count = len(twitter.friends.list())

for n in range(0, len(results["ids"]), count):
	ids = results["ids"][n:n+count]
print("Found " + count + " friends")
print("Removing your friends, this may take a while...")

for i in range(0,len(ids)):
        results = twitter.friendships.destroy(user_id = ids[i])
