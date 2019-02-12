
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LagouSpider(object):
    driver_path = r'/Users/onlyone/Downloads/chromedriver'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.infos = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver,timeout=10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="pager_container"]/span[last()]')))
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
            if "pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
                time.sleep(2)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')
        for link in links:
            self.request_detail_page(link)
            time.sleep(2)

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="job-name"]')))
        source = self.driver.page_source
        self.parse_detail_page(source)
        # 爬取完当前页面的内容之后，关闭详情页；
        self.driver.close()
        #切换回列表页
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        company = html.xpath('//h2[@class="fl"]/text()')[0].strip()
        job_name = html.xpath('//span[@class="name"]/text()')[0].strip()
        job_request_spans = html.xpath('//dd[@class="job_request"]//span')
        salary = job_request_spans[0].xpath('.//text()')
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        work_years = job_request_spans[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r'[\s/]', '', work_years)
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r'[\s/]', '', education)
        desc = "".join(html.xpath('//dd[@class="job_bt"]//text()'))
        info = {
            'company':company,
            'job_name':job_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
            'desc':desc
        }
        self.infos.append(info)
        print(info)
        print('='*30)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()






