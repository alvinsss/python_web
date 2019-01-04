#    -*- coding: utf-8 -*-
'''
@author: lin
'''
def get_httpenv(http_name):

    if http_name == 'beta_1':
        url = 'http://10.255.52.21:16672'
        print ('http::::' + url)
        return url
    
    elif http_name == 'beta_2':
        url = 'http://10.255.72.42:8902'
        print ('http::::' + url)
        return url
    
#if __name__ == '__main__':
#    url = get_httpenv('beta_1')
    
    
        
        
    
