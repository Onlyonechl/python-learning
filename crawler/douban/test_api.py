

import requests

url = 'https://api-cn.faceplusplus.com/imagepp/v1/recognizetext'

key = 'VVMuZ9qBt2W7Ms8ygSwRdeEm-G_xaoo2'
secret = 'jD5MXZCogZ2IYRyc23X7h9_wNC7tzUR1'

img_url = 'https://www.fontke.com/font/16887116/'

data = {'api_key':key,'api_secret':secret,'image_url':img_url}

response = requests.post(url,data=data)

content = response.text
if content:
    print(content)
