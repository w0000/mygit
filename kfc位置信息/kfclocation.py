import requests
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '南通',
        'pid':'',
        'pageIndex': '11',
        'pageSize': '10'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    rsp = requests.post(url=url,data=data,headers = headers)
    data_list = rsp.text
    print(data_list)