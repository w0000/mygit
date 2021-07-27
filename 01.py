import requests
if __name__ == '__main__':
    keyword = input("key:")
    url = 'https://www.baidu.com/s'
    par = {
        "ie" : "UTF - 8",
        "wd": keyword
    }
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

    rsp = requests.get(url=url,params=par,headers=headers)
    print(rsp.text)
    page_text = rsp.text
    filename = keyword + '.html'
    with open(filename,'w+',encoding='utf-8') as fp:
        fp.write(page_text)