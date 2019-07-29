from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
data = [
        ('id','wname','year','status','company'),
        (1001,"python",2019,1,"Heraizen"),
        (1002,"Introduction to web",2018,1,"Spaneos")
    ]


for row in data:
    sheet.append(row)
wb.save("ws2.xlsx")
