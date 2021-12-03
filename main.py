import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('calicut673007@gmail.com', PASSWORD)
server.sendmail(
    'calicut673007@gmail.com',
    'calicut673007@gmail.com',
    'hsgdugfh'
)