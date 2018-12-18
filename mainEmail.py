import smtplib

def sendEmail(email, emailTo, senha, mensagem, server):
    smtp = smtplib.SMTP(server, 587)
    smtp.starttls()
    smtp.login(email, senha)

    if (smtp.sendmail(email, emailTo, mensagem) == {}):
        return True
    else :
        return False
    smtp.quit()

    pass
