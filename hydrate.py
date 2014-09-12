# https://dev.twitter.com/rest/reference/get/statuses/lookup
#
import csv
import mytwitter as twitter
import time,sys
import dumptruck
import logging
import json,os 
import datetime
import re

logger=logging.getLogger(__name__)
logging.basicConfig(file=sys.stderr, level=logging.DEBUG)

from credentials import credentials

api=twitter.myApi(**credentials)

def hydrate_tweets(arr) :
    logger.debug("getting {} tweets".format(len(arr)))
    return api.LookupStatuses(arr,include_entities=False,trim_user=True,do_map=True)



if __name__=='__main__' :
    if len(sys.argv)>1 and os.path.exists(sys.argv[1]) :
        f=open(sys.argv[1])
        logger.debug("Getting data from %s" % sys.argv[1])
    else :
        f=sys.stdin
        logger.debug("Getting data from stdin")
    r=csv.DictReader(f)
    ids=[]
    result=[]
    count=0
    try :
        while True :
            try :
                o=r.next()
                count=count+1
                if not re.match(r"^\d+$",o["tweet_id"]) :
                    logger.debug("strange id %s" % o["tweet_id"])
                else :
                    ids.append(o["tweet_id"])
                if len(ids)==100 :
                    result.extend(hydrate_tweets(ids))
                    ids=[]
            except StopIteration :
                result.extend(hydrate_tweets(ids))
                break
    except Exception :
        logger.exception()
    ofn="data/hydrated-{0}.json".format(datetime.datetime.now().strftime("%Y-%m-%d:%H:%M"))
    logger.debug("writing {} records to {ofn}".format(len(result),**locals()))
    json.dump(result,open(ofn,"w"))






