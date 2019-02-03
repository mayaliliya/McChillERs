import requests
import time
import matplotlib.pyplot as plt
#import Image

# initializing variable data
max_occupancy = 30
occupancy = 0
vacancy = 0

# cisco data from MV
ZONE = "0"
url_1 = "https://n61.meraki.com/api/v0/devices/Q2GV-343J-G4CZ/camera/analytics/live"
url_2 = "https://n61.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/live"
url_3 = "https://n61.meraki.com/api/v0/devices/Q2GV-CVGT-R69W/camera/analytics/live"

def get_response(url):
    return requests.request("GET", url, data=payload, headers=headers)

def process_json(json):
    textDict = json
    # timestamp = textDict["ts"]
    zonesDict = textDict["zones"]
    personDict = zonesDict[ZONE]
    return personDict["person"]


payload = ""
headers = {
    # camera 2
    'X-Cisco-Meraki-API-Key': "c52e3bdc4349ee6eff15807deb63feaffd62c874",
    'cache-control': "no-cache",
    'Postman-Token': "2fc76385-bf31-4798-9466-6f5087c85f7b"
    }




while 1 == 0:
    time.sleep(0.5)
    # camera 1
    response1 = get_response(url_1)
    personNum1 = process_json(response.json())
    print("Camera one: {0}".format(personNum1))

    # camera 2
    response2 = get_response(url_2)
    personNum2 = process_json(response.json())
    print("Camera two: {0}".format(personNum2))

    # camera 3
    response3 = get_response(url_3)
    personNum3 = process_json(response.json())
    print("Camera three: {0}".format(personNum3))


    # Pie Chart graphics
    labels = 'Vacancy', 'Occupancy'
    occupancy = personNum
    vacancy = max_occupancy - occupancy
    sizes = [vacancy, occupancy]
    colors = ['green', 'red']
    explode = (0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors)
    plt.axis('equal')
    plt.show()




    

