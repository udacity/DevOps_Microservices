"""Simulates client requests

Requires running server!!!

make start-api

"""

import requests
import json
import base64

#Failed Query Parameters Simulation
url = "http://0.0.0.0:5001/api/aggregate"
with open("../ext/input.csv", "rb") as f:
    data = base64.b64encode(f.read())
payload = {'column':'count'} #Not enough parameters
headers = {'Content-Type': 'application/json'}
r = requests.put(url, data=data, params=payload, headers=headers)
print("status code: ", r.status_code)
print("response body: ", json.loads(r.content))

# Should get this:
# 2017-06-19 20:40:17,915 - __main__ - INFO - Content-Type is set to:  application/json
# 2017-06-19 20:40:17,915 - __main__ - INFO - Request Query String: b'column=count'
# 2017-06-19 20:40:17,916 - __main__ - INFO - column: [count] and group_by: [None] Query Parameter values
# 2017-06-19 20:40:17,916 - __main__ - INFO - Query Parameter column or group_by not set
# 127.0.0.1 - - [19/Jun/2017 20:40:17] "PUT /api/aggregate?column=count HTTP/1.1" 400 -

#Successful Query Parameters Simulation
url = "http://0.0.0.0:5001/api/aggregate"
with open("../ext/input.csv", "rb") as f:
    data = base64.b64encode(f.read())
payload = {'column':'count', 'group_by': 'last_name'} 
headers = {'Content-Type': 'application/json'}
r = requests.put(url, data=data, params=payload, headers=headers)
print("status code: ", r.status_code)
print("response body: ", json.loads(r.content))

# Should get this:
# 2017-06-19 20:40:17,919 - __main__ - INFO - Content-Type is set to:  application/json
# 2017-06-19 20:40:17,919 - __main__ - INFO - Request Query String: b'column=count&group_by=last_name'
# 2017-06-19 20:40:17,919 - __main__ - INFO - column: [count] and group_by: [last_name] Query Parameter values
# 2017-06-19 20:40:17,919 - __main__ - INFO - Decoding data of size: 161
# 2017-06-19 20:40:17,927 - __main__ - INFO - {"first_name":{"3":"john","10":"piers","15":"sam","17":"kristen","19":"john"},"last_name":{"3":"lee","10":"smith","15":"eagle","17":"smith","19":"eagle"}}
# 127.0.0.1 - - [19/Jun/2017 20:40:17] "PUT /api/aggregate?column=count&group_by=last_name HTTP/1.1" 200 -
