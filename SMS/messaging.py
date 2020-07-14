from twilio.rest import Client

#twilio_generated_account_sid
account_sid = 'A***************************'
#twilio_generated_auth_token
auth_token = '********************************'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='recievers_number',
                        from_='twilio_generated_number'
                    )

print(call.sid)
