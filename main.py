import requests
from lxml import etree
# 发给谁
url = "https://www.hetushu.com/book/5626/4196405.html"
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 发送请求
resp = requests.get(url,headers = headers)
resp.encoding="UTF-8"  # 转UTF-8
# 响应信息
# print(resp.text)


e = etree.HTML(resp.text)
title = e.xpath('//h2/text()')[0]


    # ···/text() 取文本内容
paragraphs = '\n'.join(e.xpath('//div[@id="content"]/div/text()')) # ···/text() 取文本内容


# 保存文件
with open('D:/AnYujian/Desktop/斗罗大陆IV终极斗罗.txt','w',encoding='UTF-8') as f:
    f.write(title + '\n\n' + paragraphs + '\n\n')


while True:
# 伪装自己
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 发送请求
    resp = requests.get(url,headers = headers)
    resp.encoding="UTF-8"  # 转UTF-8
# 响应信息
# print(resp.text)


    e = etree.HTML(resp.text)
    title = e.xpath('//h2/text()')[0]


    # ···/text() 取文本内容 ·XPath语法
    paragraphs = '\n'.join(e.xpath('//div[@id="content"]/div/text()')) # ···/text() 取文本内容


# 保存文件
    with open('D:/AnYujian/Desktop/斗罗大陆IV终极斗罗.txt','a',encoding='UTF-8') as f:
        f.write(title + '\n\n' + paragraphs + '\n\n')

    next_url = e.xpath('//a[@id="next"]/@href')[0]
    url = f"https://www.hetushu.com{next_url}"


# e.xpath解析出来的始终是列表