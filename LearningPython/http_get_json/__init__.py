import requests;
import json;

from http_get_json.constants import  *

print(str(url));

response = requests.get(url);

jsonData = json.loads(response.text)

for item in jsonData:
    print("EMAIL : " + item.get('email') + "\n" )
    