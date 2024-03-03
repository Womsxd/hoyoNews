import json
import time
import httpx

params = {'iAppId': 32, 'iChanId': 396, 'iPageSize': 100, 'iPage': 0, 'sLangKey': 'zh-tw'}
url = "https://api-os-takumi-static.hoyoverse.com/content_v2_user/app/a1b1f9d3315447cc/getContentList"

headers = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                "Safari/537.36",
  'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
  'DNT': "1",
  'Origin': "https://genshin.hoyoverse.com",
  'Referer': "https://genshin.hoyoverse.com/",
  'Sec-Fetch-Dest': "empty",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Site': "same-site"
}

all_detail = {}

with httpx.Client(headers=headers) as client:
    for i in range(1, 2 + 1):
        params['iPage'] = i
        resp = client.get(url=url, params=params)
        for item in resp.json()['data']['list']:
            if '祈願' in item['sTitle']:
                all_detail[item['iInfoId']] = item["sTitle"]
        time.sleep(3)
with open('all_detail.json', 'w', encoding='utf-8') as f:
    json.dump(all_detail, f, ensure_ascii=False, indent=4)

