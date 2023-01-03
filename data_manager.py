import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endp=""#addlinks
        self.response=requests.get(url=self.sheety_endp)
        self.dict=self.response.json()
        self.cities=[self.dict["prices"][i]["city"] for i in range(0,len(self.dict["prices"]))]
        self.prices=[self.dict["prices"][i]["lowestPrice"] for i in range(0,len(self.dict["prices"]))]
        self.iatacodes=[self.dict["prices"][i]["iataCode"] for i in range(0,len(self.dict["prices"]))]
    def updateprice(self,price,index): #id=i+2
        self.price=price
        self.index=index
        self.putsheetyendp=f"/{self.index+2}"#addlinks
        self.response=requests.put(url=self.putsheetyendp,json={"price":{"lowestPrice":f"{self.price}"}})


