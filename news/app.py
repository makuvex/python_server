# -*- coding: utf-8 -*-

from gnewsclient_in import MyNewsClient
from pprint import pprint

client = MyNewsClient(language='korean', location='Republic of Korea', topic='Top Stories', max_results=5)
#client = MyNewsClient(language='korean', location='Republic of Korea', topic='Top Stories', use_opengraph=True, max_results=3)

#client.get_config()
#client.topic = 'Sports'
pprint(client.get_news())
#print(client.locations)
#print(client.languages)
#print(client.topics)