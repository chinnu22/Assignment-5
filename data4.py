import json

try:
    with open("ws3.json","r") as file:
        ws_lst = json.load(file)
        for w in ws_lst:
            print(f"ID:{w['id']} Name:{w['wname']} Year:{w['year']} Status:{w['status']} Company:{w['company']}")

except Exception as e:
    print(str(e))