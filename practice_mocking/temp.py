import requests

res = requests.get("https://httpbin.org/get")
res.apparent_encoding