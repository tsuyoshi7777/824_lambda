import selenium_scraping, send_to_sqs, api_scraping
import re
from lxml import etree

pattern_amazon  = r"https?://www.amazon.co.jp[\w/:%#\$&\?\(\)~\.=\+\-]+"
pattern_rakuten = r"https?://\w+.rakuten.co.jp[\w/:%#\$&\?\(\)~\.=\+\-]+"

# lambda_read_dynamodb.py → sqs(データベースデータ) → Crawling.py
def lambda_handler(event, context):
    for record in event["Records"]:
       payload = record["body"]
       payload = eval(payload)
       url     = payload["url"]
       name    = payload["name"]
        # AMAZONの場合（URLスクレイピング）
       if re.match(pattern_amazon, url):
           add_stock            = selenium_scraping.scraping(url)
           payload["add_stock"] = add_stock
           print("payload_add_stock", payload, sep="\n")
           queue_name           = "sqs_stock_check"

           send_to_sqs.send_to_sqs(payload, queue_name)
           # → sqs(add_stock) → Check.py

        # 楽天の場合（API）
       elif re.match(pattern_rakuten, url):
           add_stock            = api_scraping.api_scraping(name)
           payload["add_stock"] = add_stock
           print("payload_add_stock", payload, sep="\n")
           queue_name           = "sqs_stock_check"

           send_to_sqs.send_to_sqs(payload, queue_name)
           # → sqs(add_stock) → Check.py
