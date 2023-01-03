from twilio.rest import Client
import smtplib
class NotificationManager:
    def __init__(self,price,city,departure,return1):
        self.price=price
        self.city=city
        self.departure=departure
        self.return1=return1
        self.msg=f"Low price Alert!!\nOnly {self.price} rupees to fly from Delhi\nto {self.city} from {departure} to {self.return1}."
    def whatsapp(self):
        account_sid = ""#add sid and autjtok
        auth_token = ""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=msg,
            from_='whatsapp:',
            to='whatsapp:'#addnum
        )
        print(message.status)
    def sendmail(self):
        connection=smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user="divyamautomated@gmail.com",password="") #addpass
        connection.sendmail(from_addr="divyamautomated@gmail.com",to_addrs="divyamautomated@gmail.com",msg=self.msg)
        connection.close()