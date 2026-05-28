"""
//////////////////////////////////////////////////////////////////////
//  Imports
//////////////////////////////////////////////////////////////////////
"""

import requests
import json

"""
//////////////////////////////////////////////////////////////////////
//  Method name : fetch_reddit_post()
//////////////////////////////////////////////////////////////////////
"""

def fetch_reddit_post(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/top.json"

    params = {
        "limit" : 5,
    }

    headers = {
        "User-Agent" : "reddit-fetcher/1.0"
    }

    r = requests.get(url, headers = headers, params = params)

    data = r.json()
    pretty_data = json.dumps(data, indent = 4)
    #print(pretty_data)

    count = 1
    for i in data["data"]["children"]:

        if i["data"]["title"] == "":

            post = i["data"]["crosspost_parent_list"][0]["title"]
            likes = i["data"]["crosspost_parent_list"][0]["score"]
            comments = i["data"]["crosspost_parent_list"][0]["num_comments"]
            link = i["data"]["crosspost_parent_list"][0]["url"]

            print("----------------------------------------------------------------")
            print(f"{count}. {post}\n")
            print(f"👍 Likes : {likes}  | 💬 Comments : {comments}")
            print(f"🔗link : {link}")
            print("----------------------------------------------------------------\n\n")

        else:

            post = i["data"]["title"]
            likes = i["data"]["score"]
            comments = i["data"]["num_comments"]
            link = i["data"]["url"]

            print("----------------------------------------------------------------")
            print(f"{count}. {post}\n")
            print(f"👍 Likes : {likes}  | 💬 Comments : {comments}")
            print(f"🔗link : {link}")
            print("----------------------------------------------------------------\n\n")

        count = count + 1

"""
//////////////////////////////////////////////////////////////////////
//  Main
//////////////////////////////////////////////////////////////////////
"""

fetch_reddit_post("laptop")


"""
//////////////////////////////////////////////////////////////////////
//  END
//////////////////////////////////////////////////////////////////////
"""