from premailer import transform
from email.message import EmailMessage
import smtplib
 
def email_recuperar_senha(template, destinatario, url=None, token=None, senha=None):
    
    try:

        if senha:
            template = template.replace("@senha", senha)
        
        if token:
            template = template.replace("@token", token)
        
        if url:
            template = template.replace("@url", url)
            
        #email pelo google
        email_from = "ajudaaiacoeshumanitarias@gmail.com"
        email_to = destinatario
        msg = EmailMessage()
        msg.add_alternative(transform(template), subtype='html')
        msg['Subject'] = "Recuperação de senha"
        msg['From'] = email_from
        msg['To'] = email_to
        
        # create server
        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login("ajudaaiacoeshumanitarias@gmail.com", "ajudaai2021")
        
        # send the message via the server.
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()
        return True
        
    except Exception as error:
        print(str(error))
        return False

def email_edicao_evento(template, destinatarios, nomeevento=None):
    
    try:
        if nomeevento:
            template = template.replace("@nomeevento", nomeevento)

        for destinatario in destinatarios:  
            #email pelo google
            email_from = "ajudaaiacoeshumanitarias@gmail.com"
            email_to = destinatario
            msg = EmailMessage()
            msg.add_alternative(transform(template), subtype='html')
            msg['Subject'] = "Evento alterado!"
            msg['From'] = email_from
            msg['To'] = email_to
            
            # create server
            server = smtplib.SMTP('smtp.gmail.com')
            server.starttls()
            
            # Login Credentials for sending the mail
            server.login("ajudaaiacoeshumanitarias@gmail.com", "ajudaai2021")
            
            try:
                # send the message via the server.
                server.sendmail(email_from, email_to, msg.as_string())
                server.quit()

            except:
                pass
            
        return True
        
    except Exception as error:
        print(str(error))
        return False

def email_excluir_evento(template, destinatarios, nomeevento=None, 
                        nomecriador=None, telefonecriador=None, 
                        emailcriador=None):  
    try:
        if nomeevento:
            template = template.replace("@nomeevento", nomeevento)

        if nomecriador:
            template = template.replace("@nomecriador", nomecriador)
        
        if telefonecriador:
            template = template.replace("@telefonecriador", telefonecriador)

        if emailcriador:
            template = template.replace("@emailcriador", emailcriador)

        for destinatario in destinatarios:  
            #email pelo google
            email_from = "ajudaaiacoeshumanitarias@gmail.com"
            email_to = destinatario
            msg = EmailMessage()
            msg.add_alternative(transform(template), subtype='html')
            msg['Subject'] = "Evento alterado!"
            msg['From'] = email_from
            msg['To'] = email_to
            
            # create server
            server = smtplib.SMTP('smtp.gmail.com')
            server.starttls()
            
            # Login Credentials for sending the mail
            server.login("ajudaaiacoeshumanitarias@gmail.com", "ajudaai2021")
            
            try:
                # send the message via the server.
                server.sendmail(email_from, email_to, msg.as_string())
                server.quit()

            except:
                pass
            
        return True
        
    except Exception as error:
        print(str(error))
        return False