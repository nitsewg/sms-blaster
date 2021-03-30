import smtplib
import time

def blast(sender,receivers,body,count,server):
    smtpObj = smtplib.SMTP(server)
    
    x = 1
    while x < count:
        smtpObj.sendmail(sender, receivers, body)
        x += 1
        time.sleep(.5)


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
body = (input("\nWhat's the message: "))
server = (input("\nSMTP server address - Blank for localhost: "))
count = int((input("\nNumber of messages to send: ")))

carrierdict = {
    "1": "txt.att.net",
    "2": "tmomail.net",
    "3": "vtext.com",
    "4": "messaging.sprintpcs.com",
    "5": "vtext.com",
    "6": "vmobl.com",
    "7": "mmst5.tracfone.com"
}

receivers = receivervar + "@" + carrierdict[carriervar]

if server == '':
    server = 'localhost'
    
blast(sender, receivers, body, count, server)
