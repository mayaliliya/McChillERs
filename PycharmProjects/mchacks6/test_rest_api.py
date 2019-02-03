import requests
import time
import matplotlib.pyplot as plt
import numpy as np

# initializing variable data
max_occupancy = 30


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






while 1 == 1:
    time.sleep(0.5)
    # camera 1
    response1 = get_response(url_1)
    personNum1 = process_json(response1.json())
    print("Camera one: {0}".format(personNum1))

    # camera 2
    response2 = get_response(url_2)
    personNum2 = process_json(response2.json())
    print("Camera two: {0}".format(personNum2))

    # camera 3
    response3 = get_response(url_3)
    personNum3 = process_json(response3.json())
    print("Camera three: {0}".format(personNum3))


    # # Pie Chart graphics
    labels = 'Vacancy', 'Occupancy'
    occupancy1 = personNum1
    occupancy2 = personNum2
    occupancy3 = personNum3

    vacancy1 = max_occupancy - occupancy1
    vacancy2 = max_occupancy - occupancy2
    vacancy3 = max_occupancy - occupancy3

    sizes1 = [vacancy1, occupancy1]
    sizes2 = [vacancy2, occupancy2]
    sizes3 = [vacancy3, occupancy3]

    colors = ['green', 'red']
    explode = (0, 0.05)

    labels = 'Vacancy\n{0} Persons'.format(sizes1[0]), 'Occupancy\n{0} Persons'.format(sizes1[1])
    plt.pie(sizes1, shadow=True, explode=explode, labels=labels, colors=colors)
    plt.savefig('testplot1.png')

    labels = 'Vacancy\n{0} Persons'.format(sizes2[0]), 'Occupancy\n{0} Persons'.format(sizes2[1])
    plt.pie(sizes2, shadow=True, explode=explode, labels=labels, colors=colors)
    plt.savefig('testplot2.png')

    labels = 'Vacancy\n{0} Persons'.format(sizes3[0]), 'Occupancy\n{0} Persons'.format(sizes3[1])
    plt.pie(sizes3, shadow=True, explode=explode, labels=labels, colors=colors)
    plt.savefig('testplot3.png')




    

