import json
ws_list = [
    {"id":1001,"wname":"python","year":"2019","status":1,"company":"Heraizen"},
    {"id":1002,"wname":"Web","year":"2018","status":1,"company":"Spaneos"}
]

try:
    with open("ws3.json","w",newline='') as file:
        json.dump(ws_list,file,indent=4)
        
except Exception as e:
    print(str(e))