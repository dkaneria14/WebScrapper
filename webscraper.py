# Import smtplib for the actual sending function
import smtplib

# Joining Devs repo

# Import the email modules we'll need
from email.message import EmailMessage

import os
import ssl
from autoscraper import AutoScraper
url = "https://www.amazon.ca/s?k=airpods+pro+2"
wanted_list = ["$329.00", "Apple AirPods (2nd Generation)"]
scraper = AutoScraper()
result = scraper.build(url, wanted_list)
grouped_results = scraper.get_result_similar(url, grouped=True)
# print
print(grouped_results)
# dict_key_price variable contains the first dict key object name
# and then prints the value of the key. Thw reason why we are doing it this way is that
# dict key name keeps on changing whenever we run the response, so dynamically we are assinging
# the dict key name and printing its value
dict_key_prices = next(iter(grouped_results))
price = grouped_results[dict_key_prices][0]
price_of_air_pods_pro_2 = price.replace("$", "")
price_of_air_pods_pro_2 = float(price_of_air_pods_pro_2)
print(price_of_air_pods_pro_2)
print()


def sendEmail(price_of_air_pods_pro_2):
    from Google import Create_Service
    import base64
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    CLIENT_SECRET_FILE = 'here is the file location of client secret json file which is generated by your google cloud account'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = 'Price of Airpods pro is: ' + str(price_of_air_pods_pro_2)+'!'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = 'Add your email address'
    mimeMessage['subject'] = 'IMPORTANT : New Price of AirPods!!!!!'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(
        userId='me', body={'raw': raw_string}).execute()
    print(message)


if price_of_air_pods_pro_2 < 340.00:
    sendEmail(price_of_air_pods_pro_2)