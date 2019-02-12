
import requests
from lxml import etree

#域名
BASE_DOMAIN = 'http://www.dytt8.net'

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    # 注意查看网页源代码中编码方式是什么，此处是'gbk'编码
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")

    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    '''
    相当于lamda函数
    def abc(url):
         return BASE_DOMAIN+url
    
    相当于map函数 
    index = 0
    for detail_url in detail_urls:
        detail_url = abc(detail_url)
        detail_url[index] = detail_url
        index += 1
    '''
    return detail_urls

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers = HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath('//div[@id="Zoom"]')[0]
    imgs = zoomE.xpath('.//img/@src')
    cover = imgs[0]
    screenshoot = imgs[1]
    movie['cover'] = cover
    movie['screenshoot'] = screenshoot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath('.//text()')
    for index,info in enumerate(infos):
        if info.startswith('◎年　　代'):
            #将"◎年　　代"替换掉，并用strip()消除字段前后的空格
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith('◎产　　地'):
            info = parse_info(info,"◎产　　地")
            movie['country'] = info
        elif info.startswith('◎类　　别'):
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith('◎豆瓣评分'):
            info = parse_info(info,"◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith('◎片　　长'):
            info = parse_info(info,"◎片　　长")
            movie['duration'] = info
        elif info.startswith('◎导　　演'):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info
        elif info.startswith('◎主　　演'):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie["actor"] = actors
        elif info.startswith('◎简　　介'):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("◎"):
                    break
                movie["profile"] = profile

    download_url = html.xpath("//td[@bgcolor='#fdfddf']")
    movie["download_url"] = download_url

    return movie


def spider():
    movies = []
    base_url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1,2):
        #第一个for循环用来控制爬取的页数，每页有30部电影
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
    print(movies)

if __name__ == '__main__':
    spider()