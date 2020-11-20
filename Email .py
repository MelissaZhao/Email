# Using python to send Email
# Import smtplib for the actual sending function

import smtplib

import json

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders 



# Set the parameters required by smtplib
print ("read data...")
with open ("Email.json")as read_file:
    sender = json.load(read_file)
    
sender_address = "email.sender489@gmail.com"
receiver_address = "melissay.chao@gmail.com"
subject = "Python email test"

# Construct object of MIMEMultipart
message = MIMEMultipart()
message["subject"] = subject
message["from"] = sender_address
message["to"] = receiver_address


# Add email contents
mail_content = MIMEText(
            """Hi,How are you?
            Please find the attached file!
            I wish you have a nice weekend!
            
            Best Regards""",
            "plain"
)
            

# Add HTML function
html = MIMEText(
     """
    <html>
        <body>
            <h1>
                Wochened Plan 
            </h1>
            <h2>
                Saturday Hiking, Sunday Studying
            </h2>
            <h3>
                Saturday Hiking in Zermatt,Sunday Studying at home 
            </h3>
            <p>
                Perfect Plan! 
            </p>
        </body>
    </html>
    """,
    "html"
)

message.attach(mail_content)
message.attach(html)

# Add email attachment
textfile = "Attachment.txt"
with open(textfile) as file:
    Attachment =  MIMEBase("application", "octet-steam")
    Attachment.set_payload(file.read())

encoders.encode_base64(Attachment)
Attachment.add_header(
    "Content-Disposition",
    f"attachment; textfile = {textfile}",
)

message.attach(Attachment)
               
# Add pictures to email
imagefile=open('Pic.png','rb')
image = MIMEImage(imagefile.read(),_subtype="png")
image.add_header('Content-ID','<image1>')
image["Content-Disposition"] = 'attachment; filename="testimage.png"'
message.attach(image)


# Send email message
session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls() # enale security
session.login(sender["adress"], sender["password"])
text = message.as_string()
session.sendmail(sender["adress"], receiver_address, text)
session.quit()
print ('Mail Sent')
