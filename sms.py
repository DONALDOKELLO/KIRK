# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC36d7d15e2807c76335f5e63ddc522477'
auth_token = 'b98d56795a8072a3f6388f66f336bc06'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Oya...Nakupenda',
                              from_='+16286003262',
                              to='+254798502759'
                          )

print(message.sid)
