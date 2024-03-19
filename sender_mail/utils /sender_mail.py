import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from sender_mail.models import MailAccount, EmailTemplate


class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, from_email, to_email, subject, message, smpt_type: str):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Добавляем текст письма
        msg.attach(MIMEText(message, 'plain'))

        if smpt_type == 'mail':
            
            # Устанавливаем соединение с SMTP-сервером
            with smtplib.SMTP_SSL('smtp.mail.ru', 465)  as server:
                server.login(self.username, self.password)
                server.send_message(from_email, to_email, msg.as_string())


def start_sender():
    """Функция для отправки писем"""

    # Получаем все аккаунты для почты mail.ru
    accounts_mail_ru = MailAccount.objects.filter(smpt_settings__server='smtp.mail.ru')

    for account in accounts_mail_ru:
        smtp_settings = account.smpt_settings

        # Создаем экземпляр EmailSender с параметрами из MailAccount
        email_sender = EmailSender(
            smtp_server=smtp_settings.server,
            smtp_port=smtp_settings.port,
            username=account.username,
            password=account.password
        )

        # Создаем экземпляр EmailTemplate (вам нужно заменить это на ваш способ выбора шаблона)
        email_template = EmailTemplate.objects.get(name='your_template_name')

        # Отправляем письмо
        email_sender.send_email(
            from_email=account.username,
            to_email='recipient@example.com',
            subject=email_template.subject_template,
            message=email_template.body_template,
            smpt_type='mail'
        )

        # Здесь вы также можете добавить запись в очередь, лог или уведомление в зависимости от ваших требований