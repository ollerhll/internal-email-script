#!/usr/bin/python
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_mail(subject, smtp_server, secure):
    from_address = "arthurhwoodhouse@gmail.com"
    to_address   = "aatina.punjabi@oracle.com"
    body         = "I'm afraid the lemur got into the pudding cups."

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    html = "<html><head></head><body>I'm afraid the lemur got into the pudding cups.</body></html>"

    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    if secure:
        s = smtplib.SMTP_SSL(smtp_server, 465)
        s.ehlo()
        s.login("arthurhwoodhouse@gmail.com", "coarsesand")
    else:
        s = smtplib.SMTP(smtp_server)    
    s.sendmail(from_address, to_address, msg.as_string())
    s.quit()

try:
    send_mail("Lemurs", "smtp.gmail.com", true)
except:
    try:
        send_mail("Lemurs 2", "internal-mail-router.oracle.com", false)
    except:
        pass
