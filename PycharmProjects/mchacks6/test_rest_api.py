import requests
import time

def get_response(url):
    return requests.request("GET", url, data=payload, headers=headers)

def process_json(json):
    textDict = json
    # timestamp = textDict["ts"]
    zonesDict = textDict["zones"]
    personDict = zonesDict[ZONE]
    return personDict["person"]


ZONE = "0"

url_1 = "https://n61.meraki.com/api/v0/devices/Q2GV-343J-G4CZ/camera/analytics/live"
url_2 = "https://n61.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/live"
url_3 = "https://n61.meraki.com/api/v0/devices/Q2GV-CVGT-R69W/camera/analytics/live"

payload = ""
headers = {
    # camera 2
    'X-Cisco-Meraki-API-Key': "c52e3bdc4349ee6eff15807deb63feaffd62c874",
    'cache-control': "no-cache",
    'Postman-Token': "2fc76385-bf31-4798-9466-6f5087c85f7b"
    }


while 1 == 1:
    time.sleep(0.5)

    # camera 1
    response = get_response(url_1)
    personNum = process_json(response.json())
    print("Camera one: {0}".format(personNum))

    # camera 2
    response = get_response(url_2)
    personNum = process_json(response.json())
    print("Camera two: {0}".format(personNum))

    # camera 3
    response = get_response(url_3)
    personNum = process_json(response.json())
    print("Camera three: {0}".format(personNum))
    
