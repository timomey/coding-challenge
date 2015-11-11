#!/usr/bin/env python

# this program takes tweets from ../tweet_input/tweets.txt and converts the JSON format to what they should look like:
# example:
# <contents of "text" field> (timestamp: <contents of "created_at" field>)
#

import json

tweetfile_handle = open('../tweet_input/tweets.txt')

#test: only take one line
oneline = tweetfile_handle.readline()
#use json.loads to turn this line to a dictionary for easy access (alternative would be using reg.exp. - check speed)
oneline_dict = json.loads(oneline)
text = oneline_dict['text']



#go through entire file
#for line in tweetfile_handle:
#    print line.split(',"text":"')[1].split('","source')[0]
