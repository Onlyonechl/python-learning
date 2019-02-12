
import requests
from lxml import etree
import os
import re
from urllib import request

def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath('//div[@class="page-content text-center"]//img[@class="img-responsive lazy image_dta"]')
    for img in imgs:
        img_url = img.get('data-original')
        print(img_url)
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。！!]','',alt)
        suffix = os.path.split(img_url)[1]
        filename = alt + suffix
        request.urlretrieve(img_url,'imges/'+filename)

def main():
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d'%x
        parse_page(url)
        break

if __name__ == '__main__':
    main()