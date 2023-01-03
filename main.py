#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
Sheetdata=DataManager()
cities=Sheetdata.cities
prices=Sheetdata.prices
iatacodes=Sheetdata.iatacodes
for i in range(0,len(cities)):
    new=FlightSearch(iatacodes[i])
    if int(prices[i])>int(new.price):
        notify=NotificationManager(new.price,cities[i],new.departure,new.return1)
        notify.sendmail()
        Sheetdata.updateprice(new.price,i)