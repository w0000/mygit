import requests
import json
from bs4 import BeautifulSoup
import time
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'


    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    id_list = []
    rsp = requests.post(url=url,headers=headers,data=data).json()
    page_nums = rsp['pageCount']
    print(page_nums)
    for dic in rsp['list']:
        #print(dic['ID'])
        id_list.append(dic['ID'])
    inf_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    fp = open('./data_list.json','w',encoding='utf-8')
    for id in id_list:
        #time.sleep(0.5)
        inf_data = {
            'id': id
        }
        inf = requests.post(url=inf_url,headers=headers,data=inf_data).json()
        #print(inf)
        json.dump(inf,fp=fp,ensure_ascii=False,indent=2)


