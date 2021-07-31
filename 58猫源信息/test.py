import requests
from lxml import etree
import time
import re
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    f = open('cat.html','r',encoding='utf-8')
    str = f.read()
    cat_tree = etree.HTML(str)
    inf = cat_tree.xpath('//article[@class="description_con"]/text()')[0]
    print(inf)


