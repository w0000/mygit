import requests
from lxml import etree
import time
import re
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    url = 'https://nj.58.com/cat/'

    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    url_list = tree.xpath('//td[@class="t"]/a/@href')
    title_list = tree.xpath('//td[@class="t"]/a/text()')

    fp = open('cat.txt', 'w', encoding='utf-8')
    i = 0
    for c_url in url_list:
        time.sleep(5)
        data_text = requests.get(url=c_url,headers=headers).text
        cat_tree = etree.HTML(data_text)
        cat_inf = cat_tree.xpath('//article[@class="description_con"]/text()')[0]
        fp.write(title_list[i]+cat_inf+'/n')
        print(title_list[i])
        i+=1

