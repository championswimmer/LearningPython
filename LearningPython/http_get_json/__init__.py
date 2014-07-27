import requests;
from http_get_json.constants import  *

print(str(url));

r = requests.get(url);
data = r.json()
print (data)