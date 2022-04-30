import requests

def stock_availability(item):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'access_token'
    headers = {'Authorization': 'Bearer ' + access_token}

    message = 'id:'+str(item['id'])+'、商品名:「'+item['name']+'」が「在庫あり」になりました'
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

def stock_not_availability(item):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'n0CYWYzGFoDVOjK4dnyNkRqId5DlBObT7pnbdccDRf0'
    headers = {'Authorization': 'Bearer ' + access_token}

    message = 'id:'+str(item['id'])+'、商品名:「'+item['name']+'」が「在庫なし」になりました。'
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)
