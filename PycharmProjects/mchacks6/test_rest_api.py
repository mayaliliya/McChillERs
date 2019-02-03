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
url = "https://n61.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/live"

payload = ""
headers = {
    'X-Cisco-Meraki-API-Key': "c52e3bdc4349ee6eff15807deb63feaffd62c874",
    'cache-control': "no-cache",
    'Postman-Token': "2fc76385-bf31-4798-9466-6f5087c85f7b"
    }




while 1 == 0:
    time.sleep(0.5)
    response = requests.request("GET", url, data=payload, headers=headers)
    textDict = response.json()
    timestamp = textDict["ts"]
    zonesDict = textDict["zones"]
    personDict = zonesDict[ZONE]
    personNum = personDict["person"]
    print(personNum)

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




