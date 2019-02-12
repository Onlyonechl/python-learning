
import requests
import re

def parse_url(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    text = response.text
    #.不能匹配换行符，DOTALL弥补这一缺陷
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>','',content)
        contents.append(x.strip())

    peoms = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        peom = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        peoms.append(peom)
    print(peoms)


def main():
    for i in range(1,11):
        url = 'https://www.gushiwen.org/default_%s.aspx' %i
        parse_url(url)



if __name__ == '__main__':
    main()