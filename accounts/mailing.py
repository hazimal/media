import smtplib
from multiprocessing import Process, Queue
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(user, to, link):
    try:
        mail_content = link
        # The mail addresses and password
        sender_address = 'email'
        sender_pass = 'password'
        receiver_address = to
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "This is a simple mail for you %s" % user  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('mail.cdd.gov.jo', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return 'Mail Sent'
        # q.put(None)
    except Exception as e:
        print(e)

