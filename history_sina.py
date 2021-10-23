import csv
import json
import time

import requests

day = '2021-09-08'
url_format = 'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={0}' \
             '&scale=60&ma=no&datalen=20'


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


def get_change(json_in, day):
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


if __name__ == '__main__':
    all_urls, all_codes = gen_meta()
    array_len = range(len(all_urls))
    for i in array_len:
        u = all_urls[i]
        c = all_codes[i]
        response = requests.get(u)
        print(u)
        time.sleep(1)
        change = get_change(response.text, day)
        print(change)
