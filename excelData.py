from openpyxl import Workbook
import csv
import requests


# wb = Workbook()
# ws = wb.active
# ws.sheet_properties.tabColor = "1072BA"
# ws['A4'] = 'hello world'
# wb.save('balances.xlsx')
# http://hq.sinajs.cn/list=sz002307,sh600928

def get_request(bat_arr):
    query_string = ','.join(bat_arr)
    req_str = 'http://hq.sinajs.cn/list={0}'.format(query_string)
    return req_str


with open('list.csv', 'r') as f:
    batch_array = []
    request_array = []
    reader = csv.reader(f)
    for row in reader:
        code = row[0]
        num = code.split('.')[0]
        mkt = code.split('.')[1]
        code = mkt.lower() + num
        batch_array.append(code)
        if len(batch_array) == 10:
            request_string = get_request(batch_array)
            request_array.append(request_string)
            batch_array = []
    if len(batch_array) > 0:
        request_array.append(get_request(batch_array))

    all_result = []
    for request in request_array:
        print(request)
        response = requests.get(request)
        ten_batch = response.text.split(';')
        for one in ten_batch:
            if len(one) > 4:
                all_result.append(one.split('=')[1])

    for one in all_result:
        print(one)
