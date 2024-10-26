import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import os

# Define sender and receiver email addresses
sender = 'bhojamre13@gmail'
password = 'Snist@123'  # Use a secure method to store your password
receivers = ['bhojamre13@gmail.com']  # Use a list for multiple receivers

# Define email message
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = COMMASPACE.join(receivers)
msg['Subject'] = 'Attendance'

# Add CSV file attachment
filename = r'StudentDetails\StudentDetails.csv'  # Use raw string for path
try:
    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(filename)}")
        msg.attach(part)
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
    exit(1)

# Send email using SMTP server
try:
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(sender, password)
    smtpserver.sendmail(sender, receivers, msg.as_string())
    print("Email sent successfully.")
except smtplib.SMTPAuthenticationError:
    print("Error: SMTP Authentication failed. Check your username and password.")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    smtpserver.quit()
