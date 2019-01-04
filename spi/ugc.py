#    -*- coding: utf-8 -*-
'''
Created on Oct 9, 2013
@author: nicesaddle
'''
import json
import urllib.request
def find_otatts_key(ota_id):
    url = ''
    url += 'http://l-api.user.qunar.com/api/oauthinit?site='
    url += ota_id
    url += '&desc=22'
    req = urllib.request(url)
    response = urllib.request.urlopen(req)
    tempstr = response.read()
    jsonstr = json.dumps(tempstr)
    json.JSONDecoder()
    test = json.JSONDecoder().decode(tempstr)['data']
    return test['consumer_secret']
