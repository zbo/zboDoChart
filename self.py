import csv
with open('list.csv', 'r') as f:
    reader = csv.reader(f)    
    for row in reader:
        code = row[0]
        num = code.split('.')[0]
        mkt = code.split('.')[1]
        if mkt == 'SH':
            print('1'+num)
        else:
            print('0'+num)