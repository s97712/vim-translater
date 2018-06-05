
# coding: utf-8

# In[13]:


import sys

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
from hashlib import md5
import time;
import math;

def URLRequest(url, params, headers={}):
    data = urlencode(params).encode();
    request = Request(url, data, headers)
    res = urlopen(request).read().decode()
    return json.loads(res);
    
def youdao_trans(text):
    
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    verify = "ebSeFb%=XZ%T[KZ)c(sy!"
    salt = str(math.floor(time.time() * 1000))
    client = "fanyideskweb"

    sign = md5((client + text + salt + verify).encode('utf-8')).hexdigest()

    params = {
        'i': text, 
        'from': 'AUTO', 
        'to': 'AUTO', 
        'smartresult': 'dict', 
        'client': client, 
        'salt': salt, 
        'sign': sign, 
        'doctype': 'json', 
        'version': '2.1', 
        'keyfrom': 'fanyi.web', 
        'action': 'FY_BY_CLICKBUTTION', 
        'typoResult': 'false'
    }
    
    try:
        json = URLRequest(url , params, {
            'Referer': url,
            'User-Agent':'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
            'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=-123456789@0.0.0.0'
        });
    except Error:
        return "翻译失败，网络异常"

    try:
        return json['translateResult'][0][0]['tgt']
    except Error:
        return "翻译失败，API异常"

def main(argv):
    info = youdao_trans((' '.join(argv[1:])))
    sys.stdout.write(info)
    
if __name__ == "__main__":
    main(sys.argv);

