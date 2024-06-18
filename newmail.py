import smtplib
import random

def send_email():
    try:
        receiver_mails = ["720722207052@hicet.ac.in"]
        sender_email = "sasikumarsa001@gmail.com"
        sender_password = "hcki oltf qmka gpxt"
        
        # Connect to the Gmail SMTP server

        for receiver_email in receiver_mails:
            otp_number = random.randint(1000, 9999)
            print(f"Sending OTP {otp_number} to {receiver_email}")

            # Create the SMTP connection
            with smtplib.SMTP("smtp.gmail.com",587) as server:
                server.starttls()
                server.login("sasikumarsa001@gmail.com", sender_password)
                
                message = f"Subject: Your OTP\n\nYour OTP is {otp_number}"
                server.sendmail(sender_email, receiver_email, message)
                
                print("Mail sent successfully")

    except Exception as e:
        print(f"Failed to send email:")

send_email()
