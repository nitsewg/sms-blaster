import smtplib
import time

def blast(sender,receiver,message,count,server):
    smtpObj = smtplib.SMTP(server)
    
    x = 1
    while x < count:
        smtpObj.sendmail(sender,receiver,message)
        x += 1


carrierlist = [
    "AT&T", 
    "T-Mobile", 
    "Verizon", 
    "Sprint", 
    "Xfinity", 
    "Virgin", 
    "Tracfone"
    ]

x = 1

for i in carrierlist:
    print(str(x) + ". ", i)
    x += 1

carriervar = (input("\nSelect phone carrier: "))
sender = (input("\nPlease enter from address: "))
receivervar = (input("\nEnter target phone number: "))
subject = (input("\nWhat's the message: "))
server = (input("\nSMTP server address - Blank for localhost: "))
count = (input("\nNumber of messages to send: "))

carrierdict = {
    "1": "txt.att.net",
    "2": "tmomail.net",
    "3": "vtext.com",
    "4": "messaging.sprintpcs.com",
    "5": "vtext.com",
    "6": "vmobl.com",
    "7": "mmst5.tracfone.com"
}

receiver = receivervar + "@" + carrierdict[carriervar]

print(receiver)
