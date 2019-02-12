import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

proxy = {
    'http':'110.73.4.41:8123'
}

response = requests.get('http://httpbin.org/ip',headers=headers,proxies = proxy)
print(response.text)