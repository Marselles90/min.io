import uuid
from django.db import models

from django.contrib.postgres.fields import ArrayField

# P0UD436W3e57LZYJRD80 mail.ru

class SmptSetttings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    
    server = models.CharField(max_length=255, blank=True, null=True)
    port = models.CharField(max_length=255, blank=True, null=True)


class MailAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    
    smpt_settings = models.ForeignKey(SmptSetttings, on_delete=models.CASCADE)
    
    
class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    
    company_name = models.CharField(max_length=255)
    company_mail = models.CharField(max_length=255)
    
    subject_template = models.TextField()
    body_template = models.TextField()

    def __str__(self):
        return self.name


class EmailQueueItem(models.Model):
    email_message = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    queued_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.email_message.subject} - Queued at {self.queued_at}'


class EmailLog(models.Model):
    email_message = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    log_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email_message.subject} - {self.status} at {self.timestamp}'


class Notification(models.Model):
    message = models.TextField()
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification to {self.recipient} - Sent at {self.sent_at}'