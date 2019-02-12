
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

data = {
    "email":"970138074@qq.com",'password':"pythonspider"
}

url = 'http://www.renren.com/PLogin.do'

session = requests.Session()

session.post(url,data=data,headers=headers)

response = session.get('http://www.renren.com/880151247/profile')

with open('renren_requests.html','w',encoding='utf-8') as fp:
    fp.write(response.text)

