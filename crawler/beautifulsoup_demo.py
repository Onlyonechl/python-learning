
from bs4 import BeautifulSoup



html ="""
<table cellpadding="0" cellspacing="0" class="tablelist">
     <tr class="h">
      <td class="l" width="374">
       职位名称
      </td>
      <td>
       职位类别
      </td>
      <td>
       人数
      </td>
      <td>
       地点
      </td>
      <td>
       发布时间
      </td>
     </tr>
     <tr class="even">
      <td class="l square">
       <a href="position_detail.php?id=44008&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        24491-大数据运维工程师（深圳）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       深圳
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="odd">
      <td class="l square">
       <a href="position_detail.php?id=43983&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        OMG097-数据平台开发工程师（北京）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       北京
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="even">
      <td class="l square">
       <a href="position_detail.php?id=43979&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        21557-音视频专项技术测试工程师(深圳)
       </a>
       <span class="hot">
       </span>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       深圳
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="odd">
      <td class="l square">
       <a href="position_detail.php?id=43957&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        20503-AI应用Linux后台研发工程师（上海）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       上海
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="even">
      <td class="l square">
       <a href="position_detail.php?id=43961&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        20503-优图专项测试工程师（上海）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       上海
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="odd">
      <td class="l square">
       <a href="position_detail.php?id=43950&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        27087-计算机视觉/图像识别工程师（深圳）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       深圳
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="even">
      <td class="l square">
       <a href="position_detail.php?id=43952&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        23671-数据开发工程师（北京）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       北京
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="odd">
      <td class="l square">
       <a href="position_detail.php?id=43945&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        SNG04-QQ看点iOS开发工程师（上海）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       上海
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="even">
      <td class="l square">
       <a href="position_detail.php?id=43947&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        SNG11-高级数据分析师（深圳）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       2
      </td>
      <td>
       深圳
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
     <tr class="odd">
      <td class="l square">
       <a href="position_detail.php?id=43949&amp;keywords=python&amp;tid=0&amp;lid=0" target="_blank">
        25926-NLP算法高级工程师（深圳）
       </a>
      </td>
      <td>
       技术类
      </td>
      <td>
       1
      </td>
      <td>
       深圳
      </td>
      <td>
       2018-09-06
      </td>
     </tr>
"""

soup = BeautifulSoup(html,'lxml')

# 1.获取所有的tr标签
#trs = soup.find_all('tr')
#for tr in trs:
#    print(tr)
#    print('-'*30)

# 2.获取第二个tr标签
#tr = soup.find_all('tr',limit=2)[1]
#print(tr)

# 3.获取所有class等于even的tr标签
'注意此处不能直接用class,因为class是python的关键字，会冲突'
'attrs是attribute的缩写'
#trs = soup.find_all('tr',class_='even')
#trs = soup.find_all('tr',attrs={'class':'even'})
#for tr in trs:
#    print(tr)
#    print('@'*30)

# 4.将所有id等于test,class也等于test的a标签提取出来
#aList = soup.find_all('a',id='test',class_='test')
#aList = soup.find_all('a',attrs={'class':"test",'id':"test"})
#for a in aList:
#    print(a)

# 5.获取所有a标签的href属性
#aList = soup.find_all('a')
#for  a in aList:
    # 1.通过下标操作的方式
    #href = a['href']
    #print(href)
    # 2.通过attrs属性的方式
    #href = a.attrs['href']
    #print(href)

# 6.获取所有的职位(纯文本）
#trs = soup.find_all('tr')[1:]
#jobs = []
#for tr in trs:
#    job = {}
#    infos =list(tr.stripped_strings)
#    job['title'] = infos[0]
#    job['category'] = infos[1]
#    job['nums'] = infos[2]
#    job['city'] = infos[3]
#    job['pubtime'] = infos[4]
#    jobs.append(job)
#print(jobs)

trs = soup.select('')
for tr in trs:
    print(tr)
