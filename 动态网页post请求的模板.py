import requests
# 设置 GET 请求的参数
url = "https://www.jisilu.cn/data/cbnew/detail_hist/110083?___jsl=LST___t=1704707501648"  # 替换为您要请求的网址
params = {"rp": 50, "page": 1}  # 替换为您的分页参数#这个是f12中载荷的表单数据字典格式填入
# 发送 GET 请求并获取返回结果
response = requests.post(url, params=params)
# 打印返回的内容
dict1 = response.json()['rows']
for i in dict1:
    print(i)