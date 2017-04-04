#!/usr/bin/python
import twitter
import time

app_name = "TwitterWiper"
consumer_key = "q41u6JKSfgLMe9LftLw4bOsJG"
consumer_secret = "6Zl5sVmoF6OYpWWAzfIvB6aM5AGz2IsEg5Bw1adTIxHH3yspdw"

print "You'll be forwarded to a web browser in two seconds."
print

time.sleep(2)

access_key, access_secret = twitter.oauth_dance(app_name, consumer_key, consumer_secret)

print "Done."
print
print "Writing config file..."
print
f = open("config.py", "w")
f.write("#Don't show this file to anyone or you can lose your twitter account.\n")
f.write("consumer_key = '%s'" % consumer_key + "\n")
f.write("consumer_secret = '%s'" % consumer_secret + "\n")
f.write("access_key = '%s'" % access_key + "\n")
f.write("access_secret = '%s'" % access_secret + "\n")
f.close()
print "Done.Don't show config.py file to anyone or you can lose your twitter account."
