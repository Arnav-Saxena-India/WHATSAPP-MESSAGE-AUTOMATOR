'''
twilio
datetime
time
1.twilio client setup
2. user inputs
3. scheduling logic
4. send message
'''
# 1. required libraries
from twilio.rest import Client
from datetime import datetime,timedelta
import time
#2. account creadentials
account_sid='ACf0983a4de797c6803e9b91782120517a'
auth_token='e8e0935e300d636dcdcaa33ae5e2946b'
client=Client(account_sid,auth_token)

#3. design send message function
def whatsapp_message(recepient_no,message_body):
    try:
        message=client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_body,
        to=f'whatsapp:{recepient_no}'
        )
        print(f'Message sent succesfully! Message ssid:{message.sid}')
    except Exception as e:
        print("An error occured")

#4. user input
name=input('Enter the recipient name: ')
recipient_number = input("Enter the whatsapp number with country code without spaces: ")
message_body=input(f"enter the messsage you want to send to {name}: ")

#5. date time and delay
date_str=input("enter the date to send message(YYYY-MM-DD)")
time_str=input("enter the time to send the message  HH:MM in 24 hr format)")
schedule=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current=datetime.now()
time_diff=schedule-current
delay_sec=time_diff.total_seconds()

if delay_sec<=0:
    print('The specified time is in the past. plz give a new datetime')
else:
    print(f"Message scheduled for {name} at {schedule}")
# wait for scheduled message
time.sleep(delay_sec)
whatsapp_message(recipient_number,message_body)




