from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, SerializerMethodField

from .models import (
    SmptSetttings, MailAccount, EmailTemplate, EmailQueueItem, EmailLog,
    Notification
)


class EmailTemplateSerializer(ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ('id', 'name', 'company_name', 'company_mail' 'subject_template', 'body_template')


class EmailQueueItemSerializer(ModelSerializer):
    class Meta:
        model = EmailQueueItem
        fields = ('id', 'email_message', 'queued_at', 'sent_at')


class EmailLogSerializer(ModelSerializer):
    class Meta:
        model = EmailLog
        fields = ('id', 'email_message', 'status', 'log_message', 'timestamp')


class EmailSMTPConfigSerializer(ModelSerializer):
    class Meta:
        model = SmptSetttings
        fields = ('id', 'name', 'server', 'port')
    

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'message', 'recipient', 'sent_at')