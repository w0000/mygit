import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    city_name_list = tree.xpath('//div[@class="bottom"]/ul/li')
    for city in city_name_list:
        c = city.xpath('./a/text()')
        print(c)
