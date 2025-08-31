import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp_to_email(receiver_email: str, otp: str):
    sender_email = "info@bigstaruae.com"
    sender_password = "j9PYrxJ3eCZt"
    
    # Create a MIME message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your OTP for Password Reset"
    
    # Create the email body
    body = f"Your One-Time Password (OTP) for password reset is: {otp}"
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Set up the SMTP server and send the email
        with smtplib.SMTP("smtp.zoho.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to your email
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("OTP email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

