import requests
import time

ZONE = "0"

url = "https://n61.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/live"

payload = ""
headers = {
    'X-Cisco-Meraki-API-Key': "c52e3bdc4349ee6eff15807deb63feaffd62c874",
    'cache-control': "no-cache",
    'Postman-Token': "2fc76385-bf31-4798-9466-6f5087c85f7b"
    }


while 1 == 1:
    time.sleep(0.5)
    response = requests.request("GET", url, data=payload, headers=headers)
    textDict = response.json()
    timestamp = textDict["ts"]
    zonesDict = textDict["zones"]
    personDict = zonesDict[ZONE]
    personNum = personDict["person"]
    print(personNum)
    
