import csv
image_template = '<figure class="third"><img src="http://image.sinajs.cn/newchart/daily/n/{0}.gif" width="50%">'\
'<img src="http://image.sinajs.cn/newchart/min/n/{1}.gif" width="50%"></figure>'
link_template = '<http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllNewsStock/symbol/{0}.phtml>'
with open('list.csv', 'r') as f:
    reader = csv.reader(f)    
    for row in reader:
        code = row[0]
        if code[0] != 's':
            num = code.split('.')[0]
            mkt = code.split('.')[1]
            code = mkt.lower()+num
        print(link_template.format(code))
        print(image_template.format(code,code))
        print('\n')