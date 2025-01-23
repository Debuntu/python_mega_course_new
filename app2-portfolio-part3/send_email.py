import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    #created an app password using my gmail so we dont want to expose our actual gmail password.
    username = "deba25taluk@gmail.com"
    password = "tsma xecf towc wynp"

    my_context = ssl.create_default_context()
    #receiver could be any email address, I am just using mine for experimenting. 
    receiver = "deba25taluk@gmail.com"


    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


