import smtplib

my_email = "binduhegdee@gmail.com"
password = "utan tcxs nxdc uhfd"
to_email = 'binduhegde1932@gmail.com'

def smtp_sendmail():
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="HI")
    except Exception as e:
        print(f"failed: {e}")
    else:
        print("sent successfully")
smtp_sendmail()