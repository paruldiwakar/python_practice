
import smtplib # to create an smtp server
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) #open and type the message in it
email = EmailMessage()
email['from'] = 'Levi Ackerman'
email['to'] = 'recievers_email'
email['subject'] = 'YOU HAVE BEEN BLESSED BY Captain Levi !!!'

email.set_content(html.substitute({'name': 'Viprooo'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('senders_email', 'senders_password')
  smtp.send_message(email)
  print('all good boss!')




