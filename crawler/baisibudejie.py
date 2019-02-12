
from queue import Queue
import threading
import requests
from lxml import etree
import csv

gLock = threading.Lock()

class Producer(threading.Thread):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        contents = html.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
        img_urls = html.xpath('//div[@class="j-r-list-c"]//img/@data-original')
        for x in range(0,min(len(contents),len(img_urls))):
            self.joke_queue.put((contents[x],img_urls[x]))
            print('下载一条')


class Consumer(threading.Thread):
    def __init__(self, joke_queue, writer, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer

    def run(self):
        while True:
            try:
                content, img_url = self.joke_queue.get()
                gLock.acquire()
                self.writer.writerow((content, img_url))
                gLock.release()
                print('保存一条')
            except:
                break

def main():
    page_queue = Queue(50)
    joke_queue = Queue(10000)
    fp = open('baisibudejie.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content','img_url'))

    for x in range(1,51):
        url = 'http://www.budejie.com/%d'%x
        page_queue.put(url)

    for x in range(10):
        t = Producer(page_queue,joke_queue)
        t.start()

    for x in range(10):
        t = Consumer(joke_queue,writer)
        t.start()

if __name__ == '__main__':
    main()