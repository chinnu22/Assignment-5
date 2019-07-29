import csv
ws_list = [
    {"id":1001,"wname":"python","year":"2019","status":1,"company":"Heraizen"},
    {"id":1002,"wname":"Web","year":"2018","status":1,"company":"Spaneos"}
]

try:
    with open("ws2.csv","w",newline='') as file:
        heading  = ["id","wname","year","status","company"]
        obj = csv.DictWriter(file,fieldnames=heading)
        obj.writeheader()
        obj.writerows(ws_list)
        
           

except Exception as e:
    print(str(e))