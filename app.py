import time
from selenium import webdriver
import smtplib
import os
from twilio.rest import Client

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
time.sleep(40)

z ='The number is Online'
account_sid = 'AC43c829f48bde478e35fe3c9d2f3e1279'
auth_token = 'cc34ffa2b77651bfd6c5a2478434adbb'

while True:
    state = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    stateString=state.text
    if 'online' in stateString:
        print('the number is online')
        client = Client(account_sid, auth_token)
        client.messages.create(from_='+13309756745',
                               to='+919448226877',
                               body=z)
        time.sleep(300)
