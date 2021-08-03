import requests
if __name__ == '__main__':
    #输入搜索关键字
    keyword = 'ip'
    #url = 'https://www.baidu.com/s?ie=UTF-8&wd='+str(keyword)
    url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

    #关键字->参数 wd
    headers = {

                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'
              }
    rsp = requests.get(url=url,headers=headers,proxies={"http":"47.101.195.97:3128"})
    page_text = rsp.text
    filename = keyword + '.html'
    #将结果保存到本地html
    with open(filename,'w+',encoding='utf-8') as fp:
        fp.write(str(page_text))