#    -*- coding: utf-8 -*-
'''
Date: 28/06/16

@author: alvin
'''
import urllib

def h_sendredpage(http_name, user_id):
    if http_name == 'http://10.255.52.21:16672':
        #test-百分比红包
        data = {}
        data['userId'] = user_id
        data['activityId'] = 'MISS-20151020-002'
        data['prizeId'] = 'REBATE-201504-0002'
        url = http_name+'/activity/api/v0/prizeSender/send?'
        print (url)
        post_data = urllib.urlencode(data)
        
        req = urllib2.urlopen(url, post_data)
        content = req.read()

        #test-投指定金额红包
        data1 = {}
        data1['userId'] = user_id
        data1['activityId'] = 'MISS-20151020-002'
        data1['prizeId'] = 'P201606-001'
        post_data1 = urllib.urlencode(data1)
        req = urllib.request.urlopen(url, post_data1)
        content = req.read()
        print (content)
    elif http_name == 'http://10.255.72.42:8902':
         #test-百分比红包
        data = {}
        data['userId'] = user_id
        data['activityId'] = 'MISS-20151020-002'
        data['prizeId'] = 'REBATE-201504-0002'
        url = http_name+'/activity/api/v0/prizeSender/send?'
        post_data = urllib.urlencode(data)
        
        req = urllib.request.urlopen(url, post_data)
        content = req.read()
        print (content)
        
        #test-投指定金额红包
        data1 = {}
        data1['userId'] = user_id
        data1['activityId'] = 'MISS-20151020-002'
        data1['prizeId'] = 'P201606-001'
        post_data1 = urllib.urlencode(data1)
        req = urllib.request.urlopen(url, post_data1)
        content = req.read()


# if __name__ == "__main__":
#     h_sendredpage('http://10.255.52.21:16672','9232B3CB-5F29-49E2-8A64-BE44E684B6B0')
