# McChillERs - McHacks 2019
**By Maya Pavlova, Kira Wadden, Danielle Erb, Darshil Shah**
The repository stores the project code submitted for the McGill Hackathon hosted by MLH (Majour League Hacking) in 2019.

## Project Summary
The goal of the project was to help guide the public to the closest available emergency care center and walk-in clinics based on real-time patient availability. The problem space focused on connecting the public to information such as patient availability in health care environments to allow for more informed decisions - such as best clinic to travel to and best times to go to a clinic - based on real-time statistics.

The project was demoed during the hackathon and won the **Cisco Meraki Integrated Hardware Challenge**.

## Project Components
### Cisco Meraki MV Camera
The Cisco Meraki MV camera and Dashboard API was used to monitor the number of people present in a room at real time. The python script  **test_rest_api.py** was used to interact with the Dashboard API and process the number of people in a room attribute. The max occupancy was hardcorded for demo purposes.

## Web Interface
The simple, user web interface can be found at **index.html**. The interface requires the user to input their current location and whether they require an Emergency Room or a Walk-In Clinic using drop down menus. The Google GCP Map API was used for automatically loacting the address as a fill-in process.

## Twillio Messaging 
We experimented with the Twillio messaging services for the project to use as an instant messaging service. However, this part of the project was not fully completed. 
