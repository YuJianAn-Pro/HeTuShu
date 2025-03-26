import requests
from lxml import etree
# 发送
url = "https://www.hetushu.com/book/5626/4196405.html"

# 伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 请求
resp = requests.get(url,headers = headers)
resp.encoding="UTF-8"  # 转UTF-8
# 响应
# print(resp.text)

e = etree.HTML(resp.text) # 解析网页
title = e.xpath('//h2/text()')[0]   # ···/text() 取文本内容
paragraphs = '\n'.join(e.xpath('//div[@id="content"]/div/text()')) # ···/text() 取文本内容

# print(title)

# print(info)

# 保存

with open('D:/AnYujian/Desktop/斗罗大陆IV终极斗罗.txt','w',encoding='UTF-8') as f:
    f.write(title + '\n\n' + p + '\n\n')
