import csv
image_template = '<figure class="third"><img src="http://image.sinajs.cn/newchart/daily/n/{0}.gif" width="50%">'\
'<img src="http://image.sinajs.cn/newchart/min/n/{1}.gif" width="50%"></figure>'
with open('list.csv', 'r') as f:
    reader = csv.reader(f)    
    for row in reader:
        print(image_template.format(row[0],row[0]))