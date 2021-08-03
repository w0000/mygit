# from codet import Chaojiying_Client
# import requests
# from lxml import etree
# if __name__ == '__main__':
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
#                 }
#     url = 'https://so.gushiwen.cn/RandCode.ashx'
#     sesson =requests.session()
#     code_img_data = sesson.get(url=url,headers=headers).content
#     # tree = etree.HTML(login_page)
#     # code_img_url = 'https://so.gushiwen.cn'+tree.xpath('//img[@id="imgCode"]/@src')[0]
#     # print(code_img_url)
#     # code_img_data = requests.get(code_img_url).content
#     with open('code.jpg','wb') as fp:
#         fp.write(code_img_data)
#
#     chaojiying = Chaojiying_Client('wi0i0i', 'lxyd2110', '920413')	#用户中心>>软件ID 生成一个替换 96001
#     im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#     #print (chaojiying.PostPic(im, 1902)	)
#     pic_str = chaojiying.PostPic(im, 1902)['pic_str']
#     print(pic_str)
#
#     headers = {
#         'referer': 'https: // so.gushiwen.cn / user / login.aspx?from=http: // so.gushiwen.cn / user / collect.aspx',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
#     }
#     log_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
#     data = {
#         '__VIEWSTATE': 'AVP2UqKeeCzJep4Lb05tbFRvGOQjFCxVHE / EFBHpF + W + +3eo2R8m6hLLw + FLJNXGm1wVguwWRixwR3U84ig2ifnQJyjcBkLZdLzBWvC7t5XiZvnXcLnVaofhEtk =',
#     '__VIEWSTATEGENERATOR': 'C93BE1AE',
#     'from': 'http://so.gushiwen.cn/user/collect.aspx',
#     'email': '3059519959@qq.com',
#     'pwd': '123qwe',
#     'code': pic_str,
#     'denglu': '登录'
#     }
#     response = sesson.post(url = log_url,headers = headers,data=data)
#     print(response.status_code)
#     with open('log.html','w',encoding='utf-8') as fp:
#         fp.write(response.text)
from codet import Chaojiying_Client
import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
                }
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    #利用session保存cookie信息
    sesson =requests.session()
    #登录界面
    log_page_text = sesson.get(url=url,headers=headers).text
    tree = etree.HTML(log_page_text)
    #验证码图片链接
    code_img_url = 'https://so.gushiwen.cn'+tree.xpath('//img[@id="imgCode"]/@src')[0]
    print(code_img_url)
    #获取验证码内容，每次请求验证码内容都会更改，利用session保存最后一次更新的cookie
    code_img_data = sesson.get(code_img_url).content
    with open('code.jpg','wb') as fp:
        fp.write(code_img_data)

    chaojiying = Chaojiying_Client('wi0i0i', 'lxyd2110', '920413')	#用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    #print (chaojiying.PostPic(im, 1902)	)
    pic_str = chaojiying.PostPic(im, 1902)['pic_str']
    print(pic_str)
    #点击登录按钮，产生的请求
    headers = {
        'referer': 'https: // so.gushiwen.cn / user / login.aspx?from=http: // so.gushiwen.cn / user / collect.aspx',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    log_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    data = {
        '__VIEWSTATE': 'AVP2UqKeeCzJep4Lb05tbFRvGOQjFCxVHE / EFBHpF + W + +3eo2R8m6hLLw + FLJNXGm1wVguwWRixwR3U84ig2ifnQJyjcBkLZdLzBWvC7t5XiZvnXcLnVaofhEtk =',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '3059519959@qq.com',
    'pwd': '123qwe',
    'code': pic_str,
    'denglu': '登录'
    }
    #利用session保存的cookie，保持会话，保证验证码内容一致，
    response = sesson.post(url = log_url,headers = headers,data=data)
    print(response.status_code)
    with open('log.html','w',encoding='utf-8') as fp:
        fp.write(response.text)