import requests
import json
if __name__ == '__main__':
    '''
    ajax局部刷新，post，请求参数，response-json类型
    '''
    word = input("word\n")
    url = 'https://fanyi.baidu.com/sug'.format(word)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    data = {
        "kw" : word
    }
    response = requests.post(url=url,data=data,headers=headers)
    rsp_text = response.json()
    print(rsp_text)
    filename = word + '.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(rsp_text,fp=fp,ensure_ascii=False)#中文