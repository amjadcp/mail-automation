import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('FROM GMAIL', 'PASSWORD')
server.sendmail(
    'FROM GMAIL',
    'TO GMAIL',
    'MESSAGE'
)