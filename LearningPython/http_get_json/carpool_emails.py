'''
Created on 27-Jul-2014

@author: arnav
'''
import requests;
import json;

from constants import  *

print(str(url));

response = requests.get(url);

jsonData = json.loads(response.text)

for item in jsonData:
    print("EMAIL : " + item.get('email') + "\n" )
    