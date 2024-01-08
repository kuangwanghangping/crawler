import requests
from bs4 import BeautifulSoup
import json

# 发送 GET 请求获取网页内容
url = "https://www.jisilu.cn/webapi/cb/list/"  # 替换为您要抓取的网页地址
response = requests.get(url)

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(response.text, "html.parser")
dict_data = json.loads(str(soup))#这步是将soup格式转换为字典格式
# 提取需要的数据
# 这里假设您要抓取网页中的标题和正文内容
print(dict_data)