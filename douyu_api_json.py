import requests
import json


class DY:
    def __init__(self):
        self.url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
        self.offset = 0

        #json格式保存
        self.f = open('dy.json', 'a', encoding='utf-8')

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
                    self.json_save(item)
            else:
                self.f.close()
                break

    def json_save(self, item):
        json.dump(item, self.f, ensure_ascii=False)
        self.f.write(',\n')


if __name__ == '__main__':
    dy = DY()
    dy.parsePage()
