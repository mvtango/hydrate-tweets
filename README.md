hydrate-tweets
==============

Given a collection of Tweet IDs, get stats about retweets, favs and other metadata.

Depends on:

-  python-twitter
-  getting credentials for twitter and putting them into a file named credentials.py (see credentials-example.py)


Bugs to fix:

- doesn't wait if it exceeds the twitter API rate limit, should use python-twitters api.GetAverageSleepTime("/statuses/lookup.json")
