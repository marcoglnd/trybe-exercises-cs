import requests
from requests.structures import CaseInsensitiveDict

r = requests.get('https://google.com')
print(r.status_code)

# url = "https://reqbin.com/echo/post/json"

# headers = CaseInsensitiveDict()
# headers["Content-Type"] = "application/json"

# data = '{"login":"my_login","password":"my_password"}'

# resp = requests.post(url, headers=headers, data=data)

# print(resp.json())
