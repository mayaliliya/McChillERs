from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACeef380399baab5f544f834b7cf1134f0'
auth_token = '906cd7162542650c8d24cfd2623f6048'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Eyyyyyyy How you doin?',
         from_='+16475564667',
         to='+16474606935'
     )

print(message.sid)