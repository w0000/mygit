import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    rsp_text = requests.get(url=url,headers=headers).content
    soup = BeautifulSoup(rsp_text,'lxml')
    #print(soup.select('.book-mulu > ul > li'))
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('sg.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        #print(detail_url)
        detail_text = requests.get(url=detail_url,headers=headers).content
        detail_soup = BeautifulSoup(detail_text,'lxml')
        detail = detail_soup.find('div',class_='chapter_content').text
        #print(detail)
        fp.write(title + '\n' + detail + '\n')
        print(title)
