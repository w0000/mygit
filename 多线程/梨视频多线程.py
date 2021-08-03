import requests
from lxml import etree
import time
import os
from multiprocessing import Pool

filepath = 'D:/PYT/video/'
def get_page_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    page_text = requests.get(url=url,headers=headers).text
    return page_text

def get_video_page_url(page_text):
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//li[@class="categoryem"]')
    video_page_urls = []
    print('url list:\n')
    for li in li_list:
        video_page_url =li.xpath('./div/a/@href')[0]
        video_page_urls.append('https://www.pearvideo.com/' + video_page_url)
        print(video_page_url)

    return video_page_urls

def get_video_url(url):
    #获取视频下载链接
    headers = {
        'Referer': url,

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    contId = url.split('_')[-1]
    video_url = 'https://www.pearvideo.com/videoStatus.jsp'
    para = {
        'contId': contId,
        'mrd': '0.38177687506833946'
    }
    mp4_url_response = requests.get(url=video_url,headers=headers,params=para).json()
    mp4_url = mp4_url_response['videoInfo']['videos']['srcUrl']

    mp4_url = mp4_url.replace(mp4_url.split('-')[0].split('/')[-1],'cont-' + str(contId))
    print(mp4_url)
    return mp4_url


def get_title(url):
    #获取中文标题
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    video_page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(video_page_text)
    titlte = tree.xpath('//div[@class="box-left clear-mar"]/h1/text()')[0]
    return titlte

def load_more_page_urls(base_page_url,no):
    #获取加载出的视频页链接
    headers = {
        'Referer': base_page_url,

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    load_url = 'https://www.pearvideo.com/category_loading.jsp?'
    params = {
        'reqType': '5',
        'categoryId': '135',
        'start': str(12*int(no)),
        'mrd': '0.5547564352582317'
    }
    load_page_text = requests.get(url=load_url,headers=headers,params=params).text
    tree = etree.HTML(load_page_text)
    li_list = tree.xpath('//li[@class="categoryem"]')
    video_urls = []
    print('url list:')
    for li in li_list:
        url = li.xpath('./div[@class="vervideo-bd"]/a/@href')[0]
        video_urls.append('https://www.pearvideo.com/' + url)
        print(url)
    return video_urls


def get_video_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    video_data = requests.get(url=url,headers=headers).content
    return video_data

def creatPath(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_video(url):
    time.sleep(0.5)
    down_url = get_video_url(url)
    title = 'video_' + url.split('_')[-1]
    video_data = get_video_data(down_url)
    fp = open(filepath + title + '.mp4', 'wb')
    fp.write(video_data)
    print("...download over..." + title)

def main():
    pool = Pool(4)
    creatPath(filepath)
    # pagenum = input("pagenum:")
    # 爬取页面数
    pagenum = 5
    curren_page_no = 0
    # 视频链接集
    video_page_urls = []
    base_page_url = 'https://www.pearvideo.com/category_135'
    while curren_page_no < pagenum:
        #获取多个页面
        video_page_urls.clear()
        if (curren_page_no == 0):
            base_page_url_text = get_page_text(base_page_url)
            video_page_urls = get_video_page_url(base_page_url_text)
        else:
            video_page_urls = load_more_page_urls(base_page_url, curren_page_no)
        curren_page_no = int(curren_page_no) + 1

        pool.map(download_video,video_page_urls)
        # for url in video_page_urls:
        #     download_video(url)

if __name__ == '__main__':
    main()

