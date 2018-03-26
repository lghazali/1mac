from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9a6031b9e43f1f246e1df1227945b4b9"
# Your Auth Token from twilio.com/console
auth_token  = "e9fa9e081c52728845b3397eaf801316"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+218912120601", 
    from_="+14154232811",
    body="Hello from Luai's SMS Service!")

print(message.sid)
