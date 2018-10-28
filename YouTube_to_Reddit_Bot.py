# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:03:05 2018

@author: Nayil
"""

import praw
import urllib
import urllib.request
import json


def get_most_recent_video():
    
    api_key = 'AIzaSyCRYBoHC4L_CYeT9LaeG3hyIc1KQLD1owo'
    channel_id = 'UCsej4tgCoXDgVH3J7M3NMgw'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    inp = urllib.request.urlopen(url)
    resp = json.load(inp)
    url_with_title = [None, None]
    for i in resp["items"]:
        if i["id"]["kind"] == "youtube#video":
            url_with_title[0] = (base_video_url + i['id']['videoId'])
            url_with_title[1] = (i["snippet"]["title"])
    print("You are about to post '" + url_with_title[1] + "' to Reddit.\n")
    return url_with_title

def post_video():
    url_with_title = get_most_recent_video()
    url = url_with_title[0]
    reddit = praw.Reddit('bot1')
    subreddits = []
    titles = []
    print('Remember that r/testingground4bots, r/testabot, r/bottesting, and r/bottest are testing grounds for bots.\n')
    sub = input("Enter the desired subreddit to post the video to. Enter 'exit' to end the list.\n")
    i = 0
    if sub != 'exit':
        title_temp = input("You are posting to r/" + sub +".Enter the desired title of your Reddit post.\n")
        titles.append(title_temp)
        while sub != 'exit':
            subreddits.append(sub)
            sub = input("Enter the desired subreddit to post the video to. Enter 'exit' to end the list.\n")
            if sub != 'exit':
                title_temp = input("You are posting to r/" + sub +".Enter the desired title of your Reddit post.\n")
                titles.append(title_temp)
                i += 1
    for i in range(len(subreddits)):
        try:
            subreddit = reddit.subreddit(subreddits[i])
            subreddit.submit(titles[i], url=url)
        except Exception as e:
            print(e)
    print(titles)
    print(subreddits)
        
def main():
    post_video()

if __name__ == "__main__":
    main()