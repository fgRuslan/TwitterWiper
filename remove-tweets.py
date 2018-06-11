from twitter import *

config = {}
try:
        exec(compile(open("config.py").read(), "config.py", 'exec'), config)
except IOError:
        print()
        print("Error: No configuration file found. Creating a new one...")
        exec(compile(open("auth.py").read(), "auth.py", 'exec'))
        exit(1)

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
results = twitter.statuses.user_timeline()

print("Removing your tweets, this may take a while...")

for status in results:
	remove_results = twitter.statuses.destroy(id = status["id"])
