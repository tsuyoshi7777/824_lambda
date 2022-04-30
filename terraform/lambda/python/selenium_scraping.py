import sys
import os
import re
import time
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver



def move_bin(
    fname: str, src_dir: str = "/var/task/bin", dest_dir: str = "/tmp/bin"
) -> None:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    dest_file = os.path.join(dest_dir, fname)
    shutil.copy2(os.path.join(src_dir, fname), dest_file)
    os.chmod(dest_file, 0o775)


def create_driver(
    options: webdriver.chrome.options.Options,
) -> webdriver.chrome.webdriver:
    driver = webdriver.Chrome(
        executable_path="/tmp/bin/chromedriver", chrome_options=options
    )
    return driver


def scraping(url):

    move_bin("headless-chromium")
    move_bin("chromedriver")

    t1 = time.time()

    options = webdriver.ChromeOptions()
    options.binary_location = "/tmp/bin/headless-chromium"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--homedir=/tmp")

    driver = create_driver(options)

    try:
        driver.get(url)

        time.sleep(5)


        stock_pattern_words = r'(在庫あり|\d+(~|-|～|ー)\d+(日|週間|か月)以内に発送|残り\d+点)'

        html = driver.page_source.encode('utf-8')

        soup = BeautifulSoup(html, 'lxml')

        availability = soup.find(id="availability")
        print('availability', availability, sep='\n')
        availability = availability.find('span')

        item_stock   = availability.get_text()

        print('item_stock', item_stock, sep='\n')

        if re.search(stock_pattern_words, item_stock):
            stock_availability = 1
            stock_availability = str(stock_availability)

            driver.close()

            driver.quit()

            t2 = time.time()

            elapsed_time = t2-t1
            print(f"経過時間：{elapsed_time:.1f}")

            return stock_availability
        else:
            stock_not_availability = 0
            stock_not_availability = str(stock_not_availability)

            driver.close()

            driver.quit()

            t2 = time.time()

            elapsed_time = t2-t1
            print(f"経過時間：{elapsed_time:.1f}")

            return stock_not_availability

    except SeleniumChromeError:
        driver.quit()
        print('エラーが出たので、chromeを終了しました')
