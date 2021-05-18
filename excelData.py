from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws1 = wb.create_sheet("Mysheet")
ws.sheet_properties.tabColor = "1072BA"
ws['A4'] = 'hello world'
wb.save('balances.xlsx')
