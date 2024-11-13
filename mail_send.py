from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Настройки почтового сервера 
class EmailSender:
    def __init__(self, sender_email, sender_password, login, smtp_server = 'smtp.mail.ru', smtp_port=465): #Конструктор класса
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.login = login
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def send_mail(self, receiver_email, subject='Завка', body='Текст'):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.login, self.sender_password)
                text = msg.as_string()
                server.sendmail(self.sender_email, [receiver_email], text)
                print('Письмо отправлено')
                return 'success'
        except Exception as e:
            print('Ошибка при отправке письма: ', e)
            return 'failed'