"""
//////////////////////////////////////////////////////////////////////
//  Imports
//////////////////////////////////////////////////////////////////////
"""

import requests
import json
import sys

"""
//////////////////////////////////////////////////////////////////////
//  Method name  : fetch_reddit_post()
//  input        : subreddit          --> name of topic
//  output       : top 5 posts on reddit on basis of subreddit
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

    try :
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

    except requests.exceptions.ConnectionError:
        print("No Internet COnnection : Try Again !")
    except requests.exceptions.Timeout:
        print("Server took too long to respond")
    except requests.exceptions.RequestException as e:
        print(e)
    except KeyError as e:
        print(f"Unexpected data structure : {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error : {e}")
    except json.JSONDecodeError:
        print("Failed to parse response.")

"""
//////////////////////////////////////////////////////////////////////
//  Main
//////////////////////////////////////////////////////////////////////
"""

subreddit = ""

if len(sys.argv) < 2:
    print("Please provide subreddit.")
    print("Usage : python reddit-post-fetcher.py <subreddit>")
    sys.exit()

subreddit = sys.argv[1]

fetch_reddit_post(subreddit)


"""
//////////////////////////////////////////////////////////////////////
//  END
//////////////////////////////////////////////////////////////////////
"""