from twilio.rest import Client

TWILIO_ACCOUNT_SID = "YOUR_SID"
TWILIO_AUTH_TOKEN = "YOUR_TOKEN"
TWILIO_SENDER = "+1XXXXXXXXXX"
TWILIO_RECEIVER = "+91XXXXXXXXXX"

def send_alert(temp, hr, activity):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = f"""
Smart Livestock Health Alert

Temperature: {temp} °C
Heart Rate: {hr} BPM
Activity: {activity}

- Automated IoT System
"""

    client.messages.create(
        body=message,
        from_=TWILIO_SENDER,
        to=TWILIO_RECEIVER
    )
