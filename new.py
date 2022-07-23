import requests

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'username': 'iEnyene',
    'password': 'feazykay5',
}

response = requests.post('https://api.makcorps.com/auth', headers=headers, json=json_data)



{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTg1NzExMzksImlhdCI6MTY1ODU2OTMzOSwibmJmIjoxNjU4NTY5MzM5LCJpZGVudGl0eSI6MTQ1MH0.OzIXvd0_IpquA-m3y2DuaMpGoXrbq2y7ghN5UkziiSE"
}

import requests

headers = {
    'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTg1NzExMzksImlhdCI6MTY1ODU2OTMzOSwibmJmIjoxNjU4NTY5MzM5LCJpZGVudGl0eSI6MTQ1MH0.OzIXvd0_IpquA-m3y2DuaMpGoXrbq2y7ghN5UkziiSE',
}

response = requests.get('https://api.makcorps.com/free/london', headers=headers)

#print(response.text)

data = response.json()
#print(data)
# import json
# new = json.loads(data)
# print(new)

#print(type(data))

#print(data.values())

dictionary = data.copy()

#print(dictionary.values())

a = dictionary.values()

'''
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTg1MjUzOTcsImlhdCI6MTY1ODUyMzU5NywibmJmIjoxNjU4NTIzNTk3LCJpZGVudGl0eSI6MTQ1MH0.w4iSLLsY4XHCaAj1Zs88W9xYNfEjjqddU09ERzrFzWY"
}
'''

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n              "username":"iEnyene",\n              "password":"feazykay5"\n      }'
#response = requests.post('https://api.makcorps.com/auth', headers=headers, data=data)

#print(response.text)

print(len(a))