import  json, ssl, urllib.request

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
context = ssl._create_unverified_context()

table="""
剩餘YouBike
| 剩餘空車架
|   |     狀態
|   |     |      站點名稱
"""

with urllib.request.urlopen(url, context=context) as jsondata:
     data = json.loads(jsondata.read().decode('utf-8-sig')) 

place = input('請輸入地點==> ')

string=table
save = '能用'
for i in data:
    if i['sna'].find(place) >= 0:
        if i['act'] == '0':
            save = '不能用'
        string+=f"{i['sbi'], str(i['bemp']).ljust(2, '0'), save, i['sna']}\n".replace("(","").replace(")","")
print(string)