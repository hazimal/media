import smtplib
from multiprocessing import Process, Queue
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject):
    try:
        mail_content = '''Hello,
        This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
        Thank You
        '''
        # The mail addresses and password
        sender_address = 'travian.hazimal@gmail.com'
        sender_pass = '1234568aa'
        receiver_address = 'hazimal@gmail.com'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = subject  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        # q.put(None)
    except Exception as e:
        print(e)

