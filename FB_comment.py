import requests
import pandas as pd

# 你的Token

token = 'EAACEdEose0cBAF8pQCQvylZAiNcBon1i2Si3dn1agke5m6XUigv800B7cK1CA4utZBVPEIuE0FpRBfGjvc6ZCdgG5B3HAWH2FO3y1nV63uu85sRyzmDb7WqSZCGEykUNrkDq6n4PLNQ8wp4RQsooJR5CTUSJV0S7FsOJdlasbNBaZBLcn1F1Uc1ZAk1TnEqT6LZAeGTMG0ZBqAZDZD'

# 目標網址

url = 'https://tw.finance.appledaily.com/daily/20180413/37985986/'

# 查詢facebook留言板ID

facebook_id = requests.get('https://graph.facebook.com/?id={}'.format(url)).json()['og_object']['id']

# 使用API來擷取留言板資訊

# order=reverse_chronological 排序依照日期，由新到舊

# filter=stream 解開留言巢狀資訊

# limit=400 一次呼叫400個留言

res = requests.get(
    'https://graph.facebook.com/v2.12/{}/comments?order=reverse_chronological&filter=stream&limit=400&access_token={}'.format(
        facebook_id, token))

# 將獲取的留言資訊先寫進list，再包成DataFrame

comments_list = []
for ele in res.json()['data']:
    comments_list.append([ele['created_time'], ele['from']['id'], ele['from']['name'], ele['message']])

df = pd.DataFrame(comments_list, columns=['時間', 'ID', '名字', '留言內容'])