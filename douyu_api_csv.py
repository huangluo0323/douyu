import requests
import json
import csv


class DY:
    def __init__(self):
        self.url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
        self.offset = 0
        self.f = open('dy.json', 'a', encoding='utf-8')

        self.csv = open('douyu.csv', 'a', encoding='utf-8', newline='')
        self.fieldname = ['room_id', 'nickname', 'vertical_src']
        self.writer = csv.DictWriter(self.csv, self.fieldname)
        self.writer.writeheader()

    def parsePage(self):
        while True:
            res = requests.get(self.url + str(self.offset))
            self.offset += 20
            zhubo_list = res.json()['data']
            if zhubo_list:
                for zhubo in zhubo_list:
                    item = {}
                    item['room_id'] = zhubo['room_id']
                    item['nickname'] = zhubo['nickname']
                    item['vertical_src'] = zhubo['vertical_src'].replace('/dy1', '')
                    # self.json_save(item)
                    self.csv_save(item)
            else:
                self.f.close()
                self.csv.close()
                break

    def json_save(self, item):
        json.dump(item, self.f, ensure_ascii=False)
        self.f.write(',\n')

    def csv_save(self, item):
        self.writer.writerow(item)


if __name__ == '__main__':
    dy = DY()
    dy.parsePage()
