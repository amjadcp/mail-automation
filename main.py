import smtplib
import requests
import time

url = 'https://api.airtable.com/v0/appWsaUGv07Sqyn3b/Table%201?maxRecords=3&view=Grid%20view'
header = {
     "Authorization": "Bearer API_KEY"
}
old_mail = ''
new_mail = ''
while True:
    r = requests.get(url, headers=header).json()
    last_index = len(r['records']) - 1
    new_email  = r['records'][last_index]['fields']['email']
    if new_email == old_mail:
        pass
    else:
        old_mail = new_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('FROM MAIL', "PASSWORD")
        server.sendmail(
            'FROM MAIL',
            new_email,
            'MESSAGE'
        )
    print("Working......")
    time.sleep(5)

