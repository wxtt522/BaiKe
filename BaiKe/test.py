import requests

headers = {
    'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
html = requests.get("http://baike.baidu.com/fenlei/%E9%87%91%E8%9E%8D",headers=headers)
print(html.text)
print(html.content.decode('utf-8'))
