# coding: utf8

from twitter import *

class myApi(Api) :

  def LookupStatuses(self,
                ids,
                trim_user=True,
                include_entities=False,
		do_map=True):
    '''
	See: https://dev.twitter.com/rest/reference/get/statuses/lookup    

    The twitter.Api instance must be authenticated.

    Args:
      id:
        The numeric ID of the status you are trying to retrieve.
      trim_user:
        When set to True, each tweet returned in a timeline will include
        a user object including only the status authors numerical ID.
        Omit this parameter to receive the complete user object. [Optional]
      include_entities:
        If False, the entities node will be disincluded.
        This node offers a variety of metadata about the tweet in a
        discreet structure, including: user_mentions, urls, and
        hashtags. [Optional]
    '''
    url = '%s/statuses/lookup.json' % (self.base_url)
    #if not self.__auth:
    #  raise TwitterError("API must be authenticated.")

    if len(ids)>100 :
      raise TwitterError("IDs can be 100 at most")
    parameters = {}

    parameters['id'] = ",".join(["%s" % id for id in ids])

    if trim_user:
      parameters['trim_user'] = 1
    if not include_entities:
      parameters['include_entities'] = 'none'
    parameters['map']=do_map     
    json = self._RequestUrl(url, 'POST', data=parameters)
    data = self._ParseAndCheckTwitter(json.content)

    return data["id"].values()


if __name__=='__main__' :
	from credentials import credentials
	import pprint
	api=myApi(**credentials)
	d=api.LookupStatuses([509944449229946880,509757731977592832])
	pprint.pprint(d)

