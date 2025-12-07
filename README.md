# 📱 WhatsApp Message Automation using Python (PyWhatKit)

This project automates WhatsApp messages using Python and the PyWhatKit library.  
It opens WhatsApp Web in your browser and sends a message to a selected number at a scheduled time.

---

## 🚀 Features
- Send WhatsApp messages automatically
- Schedule messages using hour and minute
- Works with WhatsApp Web
- Very simple and beginner-friendly

---

## 🛠️ Requirements
- Python 3.x
- Google Chrome
- WhatsApp Web logged in (scan QR once)
- Internet connection

---

## 📦 Installation

Install PyWhatKit:

```bash
pip install pywhatkit
```

---

## 📜 Usage

Create a file named **send.py** and paste:

```python
import pywhatkit

phone = "+917418132954"              # Receiver phone number with country code
message = "Hello! This is an automated WhatsApp message 😊"
hour = 12                            # 24-hour format (12 = 12 PM)
minute = 45                          # Minutes

pywhatkit.sendwhatmsg(phone, message, hour, minute)

print("Message Scheduled Successfully!")
```

Run the script:

```bash
python send.py
```

---

## ⚠️ Important Notes
- Run the script 1–2 minutes before the scheduled time.
- Your laptop must stay ON until the message is sent.
- WhatsApp Web will open automatically and send the message.
- You must stay logged into WhatsApp Web.

---

## 🧩 Project Structure

```
├── send.py
└── README.md
```

---

## 💡 Customization
You can modify this project to:
- Send multiple messages (bulk)
- Send instantly (no scheduling)
- Send to WhatsApp groups
- Add GUI interface

---

## 👨‍💻 Author
Prakash Ramakrishnan

