import requests
from lxml import etree
import time
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    page_num_max = 5
    for page_num in range(page_num_max):
        base_url ='https://www.ypppt.com/moban/list-{0}.html'.format(page_num)
        #base_url = 'https://www.ypppt.com/moban/new/index_1.html'
        base_text = requests.get(url=base_url,headers=headers).text
        #print(base_text)
        base_tree = etree.HTML(base_text)
        #主页面详情页列表
        detail_li_list = base_tree.xpath('//ul[@class="posts clear"]/li')


        for li in detail_li_list:
            time.sleep(0.1)
            #详情页链接
            detail_url = 'https://www.ypppt.com/' + li.xpath('./a[2]/@href')[0]
            detail_page = requests.get(url=detail_url,headers=headers).text
            detail_tree = etree.HTML(detail_page)

            inf_data = detail_tree.xpath('//div[@class="infoss"]')[0]
            #ppt标题
            title = inf_data.xpath('./h1/text()')[0].encode('iso-8859-1').decode('utf-8')
            #跳转链接
            dowmload_page_url = 'https://www.ypppt.com/' + inf_data.xpath('./div[@class="button"]/a/@href')[0]

            #print(dowmload_page_url)
            dowmload_page = requests.get(url=dowmload_page_url,headers=headers).text
            dowmload_tree = etree.HTML(dowmload_page)
            #zip下载链接
            dowmload_url = dowmload_tree.xpath('//ul[@class="down clear"]/li/a/@href')[0]
            #二进制流
            ppt_data = requests.get(url=dowmload_url).content
            fp = open('D:/PYT/text_resourse/ppt_download/'+title + '.zip','wb')
            fp.write(ppt_data)
            print(title)
