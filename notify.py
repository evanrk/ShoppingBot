import smtplib
import os
import config

def send_email(recipient, heading, content):
    with smtplib.SMTP(config.smtp_server, config.smtp_port) as smtp:
        # run and encrypt
        # smtp.ehlo()
        # smtp.starttls()
        # smtp.ehlo()

        # login to server
        smtp.login(config.smtp_user, config.smtp_pass)

        #subject = heading
        #body = content 
        
        subject = heading
        body = content

        msg = f'Subject: {subject}\n\n{body}'

        #sends an email
        smtp.sendmail(config.send_to, recipient, msg)
        smtp.quit()
