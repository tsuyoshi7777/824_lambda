import requests
import json

def api_scraping(name):

    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    print(name)
    payload = {
        'applicationId': applicationId,
        'hits': 5,#一度のリクエストで返してもらう最大個数（MAX30)
        # 'shopCode':'dvdoutlet',#ショップID
        'keyword': name.encode('utf-8'),
        'outOfStockFlag':0, #品切れや販売終了など購入不可の商品は結果に表示させない
        'page':1,#何ページ目か
        # 'postageFlag':1,#送料込みの商品に限定
        }
    r = requests.get(url, params=payload)
    resp = r.json()

    Items = resp['Items']
    for i in resp['Items']:
        item_r = i['Item']
        add_stock = str(item_r['availability'])

        return add_stock
