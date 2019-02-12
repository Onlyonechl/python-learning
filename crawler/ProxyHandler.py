from urllib import request

#不使用代理
#httpbin.org/ip可以用来返回当前访问来源的IP地址
#url = 'http://httpbin.org/ip'
#resp = request.urlopen(url)
#print(resp.read())

#使用代理
url = 'http://httpbin.org/ip'
#1.使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({"http":"121.31.103.27:8123"})
#2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
#3.使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())