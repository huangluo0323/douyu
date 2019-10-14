import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
#负责条件发出
from selenium.webdriver.support import expected_conditions as EC

class DouYu():
    def __init__(self):
        #斗鱼王者荣耀直播url
        self.url = 'https://www.douyu.com/g_wzry'
        self.driver = webdriver.PhantomJS()
        #设置csv格式保存信息
        self.csv = open("斗鱼_王者荣耀主播.csv","a",newline="",encoding="utf-8-sig")
        #表头信息
        self.field = ["主播","房间","主题","人气"]
        self.writer = csv.DictWriter(self.csv,fieldnames=self.field)
        #写入表头
        self.writer.writeheader()

    def get_info(self):
        '''获取信息'''
        #打开网页
        self.driver.get(self.url)
        time.sleep(3)
        #浏览器窗口最大化
        self.driver.maximize_window()
        while True:
            #等待页面加载完再执行下一步
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,'ListFooter-btn'))
            )

            li_list = self.driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
            # print(len(li_list))
            for li in li_list:
                dict1={}
                dict1["主播"]=li.find_element(By.XPATH, './/h2').text
                dict1["主题"]=li.find_element(By.XPATH, './/h3').text
                dict1["人气"]=li.find_element(By.XPATH, './/span[@class="DyListCover-hot"]').text
                dict1["房间"]=li.find_element(By.XPATH, './/a').get_attribute('href')
                print('提取数据：')
                print(dict1)

                #保存
                self.save(dict1)

            # 判断是否已提取最后一页信息
            flag = self.driver.find_element(By.CLASS_NAME, " dy-Pagination-next").get_attribute('aria-disabled')
            if flag == 'true':
                # self.csv.close()
                break

            # 点击下一页
            self.driver.find_element(By.CLASS_NAME, " dy-Pagination-next").click()

    def save(self,item):
        self.writer.writerow(item)
        print('保存成功！')

if __name__ == '__main__':
    dy = DouYu()
    dy.get_info()
















