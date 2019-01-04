#    -*- coding: utf-8 -*-
'''
Date: 10/11/13
@author: hong.liu
'''
# -*- coding:utf-8 -*-
#
# just used for a mysql test
'''
Created on 2012-3-11
@author: hong.liu
'''

def get_order_info(conn):
    cur = conn.cursor()
    cur.execute('select order_num from order_info')
    for r in cur.fetchall():
        urlstr = ('l-opb.qunar.com/api/callcenter/detail?orderNum=%s&wrapperId=wiotappb000' % (r, num))
        urlsa = 'baidu.com'
        conn = httplib.HTTPConnection(urlsa)
        result = conn.getresponse()
        content = result.read()
        print (content)
        conn.close()

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_order_info()
