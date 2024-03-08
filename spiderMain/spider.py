import os
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
import re
import time

def spider_fn(key):
    def init():
        if os.path.exists('./data.csv'):
            os.remove('./data.csv')
        with open('./data.csv', 'a', encoding='utf-8', newline='') as f:
            myWrite = csv.writer(f)
            myWrite.writerow(['type', 'title', 'price', 'buy_len',
                              'img_src', 'name', 'address', 'isFreeDelivery', 'href', 'nameHref'])

    def search_product(key):
        browser.find_element(By.ID, "q").send_keys(key)
        browser.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button').click()
        time.sleep(5)

    def get_product_details(count):
        items = browser.find_elements(By.XPATH, '//div[@class="Content--contentInner--QVTcU0M"]/div')
        scroll_position = 0
        scroll_amount = 200
        max_scroll = 4800
        for item in items:
            count = count + 1
            try:
                # 类型
                type = key
                # 商品名
                title = item.find_element(By.XPATH, './/div[@class="Title--title--jCOPvpf"]/span').text
                # 价格
                price = item.find_element(By.XPATH,
                                          './/div[@class="Price--priceWrapper--Q0Dn7pN "]/span[@class="Price--priceInt--ZlsSi_M"]').text + \
                        item.find_element(By.XPATH,
                                          './/div[@class="Price--priceWrapper--Q0Dn7pN "]/span[@class="Price--priceFloat--h2RR0RK"]').text
                # 销量
                buy_len = item.find_element(By.XPATH,
                                            './/div[@class="Price--priceWrapper--Q0Dn7pN "]/span[@class="Price--realSales--FhTZc7U"]').text
                buy_len = re.sub('[^0-9]', '', buy_len)
                # 商品图片
                img_src = item.find_element(By.XPATH, './/img[@class="MainPic--mainPic--rcLNaCv"]').get_attribute('src')
                # 店铺名
                name = item.find_element(By.XPATH, './/a[@class="ShopInfo--shopName--rg6mGmy"]').text
                # 地址
                address = item.find_element(By.XPATH, './/span[@class="Price--procity--_7Vt3mX"]').text
                # 是否包邮
                isFreeDeliveryList = ''
                try:
                    isFreeDeliveryList = item.find_elements(By.XPATH,
                                                       './/div[@class="SalesPoint--subIconWrapper--s6vanNY "]/div/span')
                    isFreeDelivery='不包邮'
                    for i in isFreeDeliveryList:
                        if i.text == '包邮':
                            isFreeDelivery = '包邮'
                except:
                    isFreeDelivery = '不包邮'
                # print(isFreeDelivery)
                # 商品链接
                href = item.find_element(By.XPATH, './/a[@class="Card--doubleCardWrapper--L2XFE73"]').get_attribute(
                    'href')
                # 店铺链接
                nameHref = item.find_element(By.XPATH, './/a[@class="ShopInfo--shopName--rg6mGmy"]').get_attribute(
                    'href')
                print(type, title, price, buy_len, img_src, name, address, isFreeDelivery, href, nameHref)
                save_to_csv(type, title, price, buy_len, img_src, name, address, isFreeDelivery, href, nameHref)
            except:
                count -= 1
                continue
            if scroll_position < max_scroll:
                scroll_script = f"window.scrollBy(0, {scroll_amount});"
                browser.execute_script(scroll_script)
                scroll_position += scroll_amount

            if count % 10 == 0:
                print('已经爬取%d条数据了' % count)
        else:
            item.find_element(By.XPATH,'//button[@class="next-btn next-medium next-btn-normal next-pagination-item next-next"]').click()
            print('正在翻页')
            time.sleep(10)
            get_product_details(count)

    def main():
        # init()
        count = 0
        search_product(key)
        get_product_details(count)
        # save_to_sql()

    def save_to_csv(type, title, price, buy_len, img_src, name, address, isFreeDelivery, href, nameHref):
        with open('./data.csv', 'a', encoding='utf-8', newline='') as f:
            myWirter = csv.writer(f, dialect='excel', delimiter=',')
            myWirter.writerow([type, title, price, buy_len, img_src, name, address, isFreeDelivery, href, nameHref])

    def save_to_sql():
        products = pd.read_csv('./data.csv')
        df = pd.DataFrame(products)
        conn = create_engine('mysql+pymysql://root:root@localhost:3306/goodsdata?charset=utf8')
        df = df_clean(df)
        df.to_sql('products', con=conn, index=False, if_exists='append')
        print('导入数据库成功')

    def df_clean(df):
        df.fillna('0', inplace=True)
        df.dropna(inplace=True)
        df.drop_duplicates(keep='last', inplace=True)
        return df

    main()


if __name__ == '__main__':
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('debuggerAddress', 'localhost:9223')
    browser = webdriver.Chrome(service=service, options=options)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    browser.get("https://www.taobao.com/")

    spider_fn('手机')