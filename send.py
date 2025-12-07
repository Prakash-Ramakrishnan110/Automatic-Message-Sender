import pywhatkit

phone = "+917418132954"              # receiver's number (with country code)
message = "Hello! This is an automated WhatsApp message 😊"
hour = 12                            # 24-hour format — 12 = 12 PM
minute = 47                          # 47 minutes

pywhatkit.sendwhatmsg(phone, message, hour, minute)

print("Message Scheduled Successfully!")
