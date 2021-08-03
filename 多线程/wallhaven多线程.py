from multiprocessing import Pool

import requests
import re
import time
import os
#爬取页数
Maxpagenum = 10
Sleeptime =0.1
def creatPath(path):
    if not os.path.exists(path):
        print("Creat path")
        os.makedirs(path)
def dowmload_pic(url):
    fpath = "D:/PYT/text_resourse/PIC"

    creatPath(path=fpath)
    print("fpath")
    # 源地址'https://wallhaven.cc/search?q=id%3A2278&sorting=random&ref=fp&seed=ZYNEUQ&page=2' 'https://wallhaven.cc/hot''https://wallhaven.cc/hot?page=4'...

    # 图片列表链接
    url = url

    print(url)
    # 初始化
    pagenum = 0
    picnum = 0
    # 获取每一个page
    while pagenum < Maxpagenum:
        headers = {
            'referer': url + 'page = ' + str(pagenum),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        pagenum = pagenum + 1
        par = {

            'page': str(pagenum)
        }
        img_data = requests.get(url=url, headers=headers, params=par).text
        # 获取图片详情页链接的正则表达式
        ex = '<a class="preview" href="(.*?)"  target="_blank"  ></a>'
        img_src_list = re.findall(ex, img_data, re.S)

        # 获取图片链接的正则表达式
        img_url_ex = '<img id="wallpaper" src="(.*?)" alt'

        # 从详情页获取图片链接
        for src in img_src_list:
            #time.sleep(Sleeptime)

            img_page = requests.get(url=src, headers=headers).text
            img_url = re.findall(img_url_ex, img_page, re.S)[0]
            img_data = requests.get(url=img_url).content
            img_name = img_url.split('/')[-1]
            img_path = fpath + '/' + img_name
            fp = open(img_path, 'wb')
            fp.write(img_data)
            print("finish " + str(picnum))
            picnum += 1


if __name__ == '__main__':
    pool = Pool(3)
    url_list=['https://wallhaven.cc/search?q=id%3A4641&page=4','https://wallhaven.cc/search?q=id%3A77513&page=2','https://wallhaven.cc/search?q=id%3A51&page=3']
    #创建文件夹路径
    pool.map(dowmload_pic,url_list)
    #dowmload_pic("https://wallhaven.cc/search?q=id%3A4641&page=4")