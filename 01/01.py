import requests
if __name__ == '__main__':
    #输入搜索关键字
    keyword = input("keyword:")
    url = 'https://www.baidu.com/s?ie=UTF-8&wd='+str(keyword)
    #关键字->参数 wd
    headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'BIDUPSID=A9CF2B5EF23713E9B3AB7A1C14D4C39C; PSTM=1615628417; '
                          'BAIDUID=BFB5E80B14EAC333F6595234A98229D4:FG=1; '
                          'BDUSS'
                          '=VMyQ2dOVWNQY345S1FBa2hnVGstNjRIbWpKbFM3WnpHS1JRQmFvaXdyc3J3WHBnRVFBQUFBJCQAAAAAAAAAAAEAAAC0nX6jxuG62rDX0~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACs0U2ArNFNgR; BDUSS_BFESS=VMyQ2dOVWNQY345S1FBa2hnVGstNjRIbWpKbFM3WnpHS1JRQmFvaXdyc3J3WHBnRVFBQUFBJCQAAAAAAAAAAAEAAAC0nX6jxuG62rDX0~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACs0U2ArNFNgR; __yjs_duid=1_bc5d8acf3d5efe6396879160d8c1727b1618473293154; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=107313_110085_127969_128698_164869_168389_175756_176678_177060_177094_177168_177370_177413_177474_178328_178602_178804_179348_179368_179402_179428_180407_180434_180435_180513_180641_180654_180757_180856_180870_181125_181218_181271_181370_181398_181428_181433_181582_181628_181646_181660_181667_181808_181827_181984_182025_182076_182194_182243_182258_182273_182331_182382_182412_182462_182550_182586_182612_182668; BDICON=10294984.98; BDPASSGATE=IlPT2AEptyoA_yiU4VKI3kIN8efRMPG4HB8JS5p63lStfCaWmhH3BrUzWz0HSieXBDP6wZTXdMsDxXTqXlVXa_EqnBsZolpOaSaXzKGoucHtVM69-t5yILXoHUE2sA8PbRhL-3MEF2ZELlMvcgjchQZrchW8z3IcnwL7hy47ifaADYjyZVm2r7m-Z9sJLCPAPNu594rXnEpKKSm0Ut0lTS8yqC1yM8gvzw0ag1A7A3D5rkoXGurSRvAa1Fz5BJV2BxCyGwC78qSo0-MvrpckVEIdnUSI7tC; delPer=0; SE_LAUNCH=5%3A1627379664; MSA_PBT=98; MSA_ZOOM=1056; BD_CK_SAM=1; BD_HOME=1; BAIDUID_BFESS=BFB5E80B14EAC333F6595234A98229D4:FG=1; COOKIE_SESSION=3839_0_9_9_25_6_0_0_9_2_1_0_3737_0_9_0_1627380134_0_1627380125%7C9%2316622_17_1627218664%7C9; BD_UPN=12314753; H_PS_645EC=c90a2NhsDXypUAYkVFE5oVmVt7WaXl0YOFIPxZuF1ec6LOHjc%2FW3M66duU4; BA_HECTOR=0081840h0k800k0k291gfvpcd0q; BDSVRTM=58; MSA_WH=300_634; MSA_PHY_WH=600_1268; wpr=0',
                'Host': 'www.baidu.com',
                'Referer': 'https://www.baidu.com/',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                'sec-ch-ua-mobile': '?1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'}
    rsp = requests.get(url=url,headers=headers)
    page_text = rsp.text
    filename = keyword + '.html'
    #将结果保存到本地html
    with open(filename,'w+',encoding='utf-8') as fp:
        fp.write(str(page_text))