#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:53:27 2020

@author: chaoyang
"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import numpy as np
import pandas as pd
import pymongo

#client = pymongo.MongoClient("mongodb://Ychao:G8Fy7euWV4ngD5fb@cluster1-shard-00-00-stdrw.mongodb.net:27017,cluster1-shard-00-01-stdrw.mongodb.net:27017,cluster1-shard-00-02-stdrw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster1-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client['Market']
#mycol = db['Cryptocurrency']
#mydict = {'name': 'BTC', 'price': 123}
#x = mycol.insert_one(mydict)


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '3c73b8c0-245b-4936-8faf-ae4a6b5d8048',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  
  #data_list = list(data.values())
  #data_list = [w.replace('{}[]','') for w in data_list]
  #content = str(data_list[1])
  #s=pd.Series(data['data'][0],index=['id','name','symbol','quote'])
  
  for i in range(0,1):
      infor_list = list(data['data'][i]['quote'].values())
      price = infor_list[0]['price']
      volume = infor_list[0]['volume_24h']
      percentc1h = infor_list[0]['percent_change_1h']
      percentc7d = infor_list[0]['percent_change_7d']
      percentc24h = infor_list[0]['percent_change_24h']
      marketc = infor_list[0]['market_cap']
      last_updated = infor_list[0]['last_updated']
      print(data['data'][i]['name'],price, volume,percentc1h,percentc7d,percentc24h,
            marketc,last_updated)
              #type(data['data'][i]['quote'].values()))
#  print(data['data'][0]['name'],data['data'][0]['quote'])
#  pd = pd.DataFrame(data['data'])
#  print(pd)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)