import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASS
from models import get_subscribers

def send_email_to_subscribers(subject, message):
    subscribers = get_subscribers()
    if not subscribers:
        return {"error": "No subscribers found."}

    #setting up email server
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        #setup email body

        for subscriber in subscribers:
            email = subscriber["email"]
            msg = MIMEMultipart()
            msg["From"] = EMAIL_USER
            msg["To"] = email
            msg["Subject"] = subject

            # Attach the message body
            msg.attach(MIMEText(message, 'plain', 'utf-8'))

            # Send the email
            server.sendmail(EMAIL_USER, email, msg.as_string())
        
        server.quit()
        return {"email" : "Email sent successfully to all subscribers"}
    except Exception as e:
        return {"error": str(e)}
