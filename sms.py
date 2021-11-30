#Send a SMS

import time
from time import sleep
from sinchsms import sinchsms

def sendsms():

    number = "your_mobile_number"
    app_key = "your_app_key"
    app_secret = "your_app_secret"


message = "Hello, How are you today?"

client = sinchsms(app_key, app_secret)
print("Sending '%s' to %s" % (message, number))

response = client.send_message(number, message)
message_id = response['messageid']
response = client.check_status(message_id)

while response['status']  !='successful':
    print(response['status'])
    time.sleep(1)
    response = client.check_status(message_id)

print(response['status'])

if _name_ = "_main_":
    sendsms()