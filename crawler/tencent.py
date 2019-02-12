
import requests
from lxml import etree

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

DOMAIN = 'https://hr.tencent.com/'

url = 'https://hr.tencent.com/position.php?keywords=python'

def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    # print(etree.tostring(html,encoding="utf-8").decode('utf-8'))
    detail_urls = html.xpath('//td[@class="l square"]/a/@href')

    detail_urls = map(lambda url: DOMAIN + url, detail_urls)

    return detail_urls

def get_profile(detail_url):
    job = {}
    response = requests.get(detail_url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)

    def combine(list):
        union = ''.join(list)
        new_list = union.strip()
        return new_list

    title = html.xpath('//tr[@class="h"]//text()')
    job['title'] = combine(title)

    zoom = html.xpath('//div[@class="box wcont_a"]')[0]
    #zoom = html.xpath('//tr[@class="c bottomline"]')[0]
    infos = zoom.xpath('.//text()')
    for index,info in enumerate(infos):
        if info.startswith("工作地点"):
            job['location'] = combine(infos[index+1])
        elif info.startswith("职位类别"):
            job['category'] = combine(infos[index+1])
        elif info.startswith("招聘人数"):
            job['nums'] = combine(infos[index+1])
        elif info.startswith("工作职责"):
            responsibility = [infos[index+1]]
            for x in range(index+1,len(infos)):
                if infos[x].startswith("工作要求"):
                    break
                responsibility.append(infos[x])
            job['responsibility'] = combine(responsibility)
        elif info.startswith("工作要求"):
            requirement = [infos[index+1]]
            for x in range(index+1,len(infos)):
                if infos[x].startswith("申请岗位"):
                    break
                requirement.append(infos[x])
            job['requirement'] = combine(requirement)

    return job


def spider():
    jobs = []
    base_url = 'https://hr.tencent.com/position.php?keywords=python&start={}#a'
    for x in range(0,1):
        url = base_url.format(x*10)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            job = get_profile(detail_url)
            jobs.append(job)
    print(jobs)

if __name__ == "__main__":
    spider()
