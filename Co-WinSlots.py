import requests
import json
from datetime import datetime
import pprint 

district_id = 149 # To get this value, firt log in to co-win portal, do an 'inspect element' and then serach with district. You'll find the code in network tab.

# 149  - south delhi
# 142  - west delhi
# etc.

date = datetime.now().strftime("%d-%m-%Y")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}", headers=headers)
#print(pprint.pformat(response.json()))
print("\nBY DISTRICT::\n")
for center in response.json()['centers']:
    print('#'*20)
    print('Name : ', center.get('name',None))
    print('Address : ', center.get('address',None))
    for session in center['sessions']:
        if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
            #print(center)
            print('Date : ',session.get('date',None),' Available Capacity : ',session.get('available_capacity',None),' Vaccine : ', session.get('vaccine',None))
            print('Slots : ', session.get('slots',None))


pincode = 110001 ####### change your pincode here

url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}"

print("\nBY PINCODE::\n")
response = requests.get(url, headers=headers)
for center in response.json()['centers']:
    print('#'*20)
    print('Name : ', center.get('name',None))
    print('Address : ', center.get('address',None))
    for session in center['sessions']:
        if  session['min_age_limit'] == 18 and session['available_capacity'] > 0:
            print('Date : ',session.get('date',None),' Available Capacity : ',session.get('available_capacity',None),' Vaccine : ', session.get('vaccine',None))
            print('Slots : ', session.get('slots',None))

