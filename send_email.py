import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_message(subject, message, reciever_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "joseph0701p@gmail.com"
    password = "oompnxjzxjtysruy"
    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = reciever_email
    msg["Subject"] = str(subject)

    # Add body to email
    msg.attach(MIMEText(message, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
