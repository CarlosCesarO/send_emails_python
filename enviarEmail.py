# -*- coding: utf-8 -*-
import smtplib
import email.message
from getMail import getEmails
from email.header import Header
from email.utils import formataddr


def enviar_email(x): 
    corpo_email = """
    
    <p>Olá, tudo bem por aí? </p>
    <p></p>
    <p></p>
    <p></p>
    <p></p>
    <p></P>
    <p>Desde já, agradecemos. &#128516;</p>
    <p>Equipe INCULCAR</p>

    """
    
    msg = email.message.Message()
    msg['Subject'] = "Convite Reunião Inculcar"
    msg['From'] = formataddr((str(Header('Inculcar', 'utf-8')), 'email'))
    msg['to'] = x
    password = 'password'
    msg.add_header('Content-Type', 'text/html',)
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login('contato@inculcar.com.br', password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

list = getEmails()

for i in list:
    enviar_email(i[0])
    print ('E-mail enviado para '+ i[0])