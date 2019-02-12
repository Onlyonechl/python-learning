
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv

class BossSpider(object):
    driver_path = r'/Users/onlyone/Downloads/chromedriver'

    def __init__(self,writer):
        self.driver = webdriver.Chrome(executable_path=BossSpider.driver_path)
        self.url = 'https://www.zhipin.com/job_detail/?query=python&scity=100010000&industry=&position='
        #self.infos = []
        self.writer = writer

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver,timeout=10).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="next"]')))
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath('//a[@class="next"]')
            if "disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
                time.sleep(2)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath('//div[@class="info-primary"]/h3[@class="name"]/a/@href')
        for link in links:
            self.request_detail_page('https://www.zhipin.com'+link)
            time.sleep(2)

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="name"]')))
        source = self.driver.page_source
        self.parse_detail_page(source)
        # 爬取完当前页面的内容之后，关闭详情页；
        self.driver.close()
        # 切换回列表页
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        company = html.xpath('//h3[@class="name"]/a/text()')[0].strip()
        job_name = html.xpath('//div[@class="name"]/h1/text()')[0].strip()
        salary = html.xpath('//span[@class="badge"]/text()')[0].strip()
        job_spans = html.xpath('//div[@class="info-primary"]/p/text()')
        city = job_spans[0].strip()
        city = re.sub('城市：', '', city)
        work_years = job_spans[1].strip()
        work_years = re.sub('经验：', '', work_years)
        education = job_spans[2].strip()
        education = re.sub('学历：', '', education)
        descs = html.xpath('//div[@class="job-sec"]/div[@class="text"]/text()')
        new_descs = []
        for desc in descs:
            desc = desc.strip()
            new_descs.append(desc)
        #info = {
            #'company':company,
            #'job_name':job_name,
            #'salary':salary,
            #'city':city,
            #'work_years':work_years,
            #'education':education,
            #'desc':new_descs
        #}
        #self.infos.append(info)
        self.writer.writerow((company,job_name,salary,city,work_years,education,new_descs))
        print('成功爬取一条信息')


if __name__ == '__main__':
    fp = open('boss.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('company','job_name','salary','city','work_years','education','desc'))
    spider = BossSpider(writer)
    spider.run()






