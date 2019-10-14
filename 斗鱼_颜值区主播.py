import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# 负责条件发出
from selenium.webdriver.support import expected_conditions as EC




class DouYu:
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.csv = open('douyu.csv', 'a', newline='', encoding='utf-8-sig')
        self.field = ['主播', '房间', '主题', '人气', '靓照']
        self.writer = csv.DictWriter(self.csv, fieldnames=self.field)
        self.writer.writeheader()  # 写入表头
        self.url = 'https://www.douyu.com/g_yz'

    def get_info(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()  # 浏览器窗口设置为最大

        while 1:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ListFooter-btn'))
            )
            # js = 'document.body.scrollTop=10000'
            # self.driver.execute_script(js)
            time.sleep(30)

            douyu_list = self.driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
            print(len(douyu_list))
            for li in douyu_list:
                # 房间标题
                title = li.find_element(By.XPATH, './/h3').text
                print(title)
                # 主播名字
                name = li.find_element(By.XPATH, './/h2').text
                # 主播图片
                print(name)
                pic_url = li.find_element(By.XPATH, './/img[@class="DyImg-content is-normal "]').get_attribute('src')
                pic = pic_url.replace('/webpdy1', '').replace('small', 'big')
                print(pic_url)
                # 关注人数
                hot = li.find_element(By.XPATH, './/span[@class="DyListCover-hot"]').text
                print(hot)
                # 房间号
                room = li.find_element(By.XPATH, './/a').get_attribute('href')
                print(room)

                item = {
                    '主播': name,
                    '房间': room,
                    '主题': title,
                    '人气': hot,
                    '靓照': pic
                }
                self.save(item)
            flag = self.driver.find_element(By.CLASS_NAME, " dy-Pagination-next").get_attribute('aria-disabled')
            if flag == 'true':
                break
            self.driver.find_element(By.CLASS_NAME, " dy-Pagination-next").click()  # 点击下一页
            # 如果下一页不能点，break

    def save(self, item):
        self.writer.writerow(item)

if __name__ == '__main__':
    dy = DouYu()
    dy.get_info()
