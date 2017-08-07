#!/usr/bin/python
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_mail(subject, host_name, host_port):
    smtp_server  = "internal-mail-router.oracle.com"
    from_address = "spinnaker-test-mail@oracle.com"
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

    s = smtplib.SMTP(smtp_server)
    s.sendmail(from_address, to_address, msg.as_string())
    s.quit()
send_mail("Lemurs", "test.com", "80")
