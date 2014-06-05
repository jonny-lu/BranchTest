# -*- coding:UTF-8 -*-
'''
Created on 2013-7-17

@author: Jonathan Lu
'''

import hmac
from hashlib import sha1
from time import time

method = 'GET'
expires = int(time() + 1200)
path = '/v1/AUTH_test/tempurl/TestPhoto1.jpg'
key = 'temp_key2'
hmac_body = '%s\n%s\n%s' % (method, expires, path)
sig = hmac.new(key, hmac_body, sha1).hexdigest()

url = 'http://172.26.181.225:8081/v1/AUTH_test/tempurl/TestPhoto1.jpg?temp_url_sig=%s&temp_url_expires=%s' % (sig, expires)

print url

