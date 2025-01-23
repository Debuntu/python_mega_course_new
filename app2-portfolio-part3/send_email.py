import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "deba25taluk@gmail.com"
    password = "tsma xecf towc wynp"

    my_context = ssl.create_default_context()
    receiver = "deba25taluk@gmail.com"


    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


