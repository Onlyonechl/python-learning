from urllib import request,parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    data={
        'telephone':'17682305670',
        'password':'chl930528'
    }
    login_url = 'http://www.renren.com/SysHome.do'
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)

def visit_profile(opener):
    dapeng_url = 'http://www.renren.com/880151247/profile'

    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(req)
    with open('renren_url.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)