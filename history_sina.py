import csv
import json
import time
import requests


url_format = 'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={0}' \
             '&scale=60&ma=no&datalen=20'

class Stock:
    def __init__(self):
        self.each_day_change = []
        self.each_day = []
        self.name = ''
        self.code = ''

def gen_meta():
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        all_codes = []
        all_urls = []
        for row in reader:
            all_codes.append(row)
            code = row[0].split('.')[0]
            mkt = row[0].split('.')[1]
            ncode = mkt + code
            url_formatted = url_format.format(ncode)
            all_urls.append(url_formatted)
        return all_urls, all_codes


def a_print(array):
    for i in array:
        print(i)


def get_change(json_in):
    json_object = json.loads(json_in)
    # print(json_object)
    last_mins = []
    all_changes = []
    for i in range(len(json_object)):
        mins = json_object[i]['day'].split(' ')[1]
        if mins == '15:00:00':
            last_mins.append(json_object[i])
    for i in range(len(last_mins))[1:]:
        date = last_mins[i]['day'].split(' ')[0]
        today_close = float(last_mins[i]['close'])
        yesterday_close = float(last_mins[i - 1]['close'])
        change_value = (today_close - yesterday_close) * 100 / yesterday_close
        all_changes.append({date: change_value})
    return all_changes


def fileExist(filename):
    import os
    if os.path.exists('./sina/{0}'.format(filename)):
        return True
    return False


if __name__ == '__main__':
    all_urls, all_codes = gen_meta()
    array_len = range(len(all_urls))
    all_changes = []
    for i in array_len:
        u = all_urls[i]
        c = all_codes[i]
        filename = c[0] + '.json'
        if not fileExist(filename):
            print('Number: {0} '.format(i) + 'web-fetch {0}'.format(u))
            response = requests.get(u)
            f_local = open('./sina/{0}'.format(filename), 'w')
            f_local.writelines(response.text)
            time.sleep(1)
            f_local.close()
        else:
            print('hit local')
        f_local = open('./sina/{0}'.format(filename), 'r')
        content = f_local.readlines()[0]
        change = get_change(content)
        all_changes.append(change)

