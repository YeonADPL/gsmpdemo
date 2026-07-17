from email.message import EmailMessage
import smtplib
import logging

logging.basicConfig(filename="smtp.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")


gsmp_smpt_server = "gsmg.poc-athenadynamics.com"
gsmp_smpt_port = 25

try:
    msg = EmailMessage()
    msg["Subject"] = "Testing iWV SASA GSMP SMTP"
    msg["From"] = "testGSMP@testing.com"
    msg["To"] = "hongyi.tan@athenadynamics.com"
    
    msg.set_content("""
    Your file has been scanned.
    Testing on 17th July 2026.
    Status: Clean
    """)
    
    try:
        with open("InteractiveDiceRoller.pdf",  "rb") as f:
            file_data = f.read()
        
        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename="InteractiveDiceRoller.pdf"
        )
    
    except FileNotFoundError:
        print("Attachment file not found.")
        logging.info("Attachment file not found.")
        raise

    with smtplib.SMTP(gsmp_smpt_server, gsmp_smpt_port) as server:
        server.set_debuglevel(1)
        server.send_message(msg)


except smtplib.SMTPRecipientsRefused as e:
    print(f"Recipient rejected: {e}")

except smtplib.SMTPSenderRefused as e:
    print(f"Sender rejected: {e}")

except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication failed: {e}")

except smtplib.SMTPConnectError as e:
    print(f"Failed to connect SMTP server: {e}")

except smtplib.SMTPException as e:
    print(f"SMTP error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")

else:
    print("Email Sent")
