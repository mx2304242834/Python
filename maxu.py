# def getMax(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     else:
#         return"相等"
# print(getMax(6,9))
#定义函数
data = bytes(urllib.parse.urlencode({'pw':'123','un':'456'},enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.requset.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)