import os
import ssl
import  smtplib
from email.message import EmailMessage
import smtplib
x=1
def mail():
    if (x == 1):
        email_sender = 'abhijithpramod91@gmail.com'
        email_password = 'aewovwtuygtakkmw'
        email_receiver = 'abhijithpramod20002@gmail.com'
        subject = 'Alert: Access Attempt Detected!!!'
        body = """Attention! Bring to your attention that our security systems have detected a recent access attempt to a user's login, which has been deemed safe and non-threatening. The system has identified.

    While there is no cause for concern regarding the security of the user's account.It's important to keep track of access attempts to ensure the overall security of our system and protect our users' information."
        """
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    else:
        print("hai")
