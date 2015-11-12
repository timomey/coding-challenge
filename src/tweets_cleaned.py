#!/usr/bin/env python

# this program takes tweets from ../tweet_input/tweets.txt and converts the JSON format to what they should look like:
# example:
# <contents of "text" field> (timestamp: <contents of "created_at" field>)
#

import json


def clean_string(text):
    text.strip()
    text.replace("\/", "/")
    text.replace("\\", "\ ")
    text.replace("\'", "'")
    text.replace('\"', '"')
    text.replace("\n", " ")
    text.replace("\t", " ")
    text = " ".join(text.split())
    return text

numberunicode = 0
numberleftout = 0
#open tweets file; note that "with ... as ..." closes file connection automatically
with open('../tweet_input/tweets.txt','r') as tweetfile_handle:
    #only take one line at a time
    for oneline in tweetfile_handle:
        #use json.loads to turn this line to a dictionary for easy access (alternative would be using reg.exp. - check speed)
        oneline_dict = json.loads(oneline)
        #from the json, the dictionary 'text' entry has the tweet
        try:
            text_u = oneline_dict['text']
            #convert it to ascii, ignoring non readable stuff. (TODO RECORD IF IT IS NOT READABLE)
            #text_ascii = text_u.encode('ascii','ignore')
            try:
                text_ascii = text_u.encode('ascii')
            except UnicodeEncodeError:
                text_ascii = text_u.encode('ascii','ignore')
                numberunicode += 1

            timestamp = oneline_dict['created_at']
            timestamp = timestamp.encode('ascii')
            cleantext = clean_string(text_ascii)
            result = cleantext + ' (timestamp: ' + timestamp + ')'

            #tweet_out = open('../tweet_output/ft1.txt','a')
            with open('../tweet_output/ft1.txt', 'a') as tweet_out:
                tweet_out.write(result)
                tweet_out.write('\n')
        except KeyError:
            numberleftout += 1

unicodeleftout = str(numberunicode) + ' tweets contained unicode.'
keyerrorcount = str(numberleftout) + ' tweets left out because of missing data.'
print unicodeleftout
print keyerrorcount
with open('../tweet_output/ft1.txt', 'a') as tweet_out:
    tweet_out.write('\n')
    tweet_out.write(unicodeleftout)
