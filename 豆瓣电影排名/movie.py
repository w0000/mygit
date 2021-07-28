import requests
import json
if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list?"
    data = {
        'type': '25',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '40'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    rsp = requests.get(url=url,params=data,headers=headers)
    data_list = rsp.json()
    fp = open('./db.json','w',encoding='utf-8')
    json.dump(data_list,fp=fp,ensure_ascii=False)
