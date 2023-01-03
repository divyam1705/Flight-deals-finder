import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,councode):
        self.tequila_api="" #addapi
        self.tequila_endp="https://tequila-api.kiwi.com/v2/search"
        self.header={"apikey":self.tequila_api}
        self.councode=councode
        self.curdate = datetime.today()
        self.m6date = self.curdate + relativedelta(months=6)
        self.parameters={"fly_from":"DEL","fly_to":self.councode,"dateFrom":self.curdate.strftime("%d/%m/%Y"),"dateTo":self.m6date.strftime("%d/%m/%Y"),
            "curr":"INR","one_for_city":1,"nights_in_dst_from":4,"nights_in_dst_to":12,"flight_type":"round"}#
        self.response=requests.get(url=self.tequila_endp,params=self.parameters,headers=self.header)
        self.departure=self.response.json()["data"][0]["local_arrival"].split("T")[0]
        self.return1=self.response.json()["data"][0]["route"][-1]["local_arrival"].split("T")[0]
        self.days=self.response.json()["data"][0]["nightsInDest"]
        self.price=(int(self.response.json()["data"][0]["price"]))



