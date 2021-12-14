import sys
import requests

cmd = 'http://hq.sinajs.cn/list=sh{0}'
request = cmd.format(sys.argv[1])
response = requests.get(request)
content = response.text.split('=')[1]
content = content[1:].split(',')
yesterday_close_prise = content[2]
now_price = content[3]
high_price = content[4]
low_price = content[5]
gap = (float(now_price) - float(yesterday_close_prise)) * \
    100 / float(yesterday_close_prise)
print(gap)