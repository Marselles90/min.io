from django.contrib.auth.models import update_last_login

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema


from utils import BaseCRUD, CustomPagination
from .models import (
    SmptSetttings, MailAccount, EmailTemplate, EmailQueueItem, EmailLog, Notification
)
from .serializer import (
   EmailTemplateSerializer, EmailQueueItemSerializer, EmailLogSerializer, EmailSMTPConfigSerializer,
   NotificationSerializer
)


class EmailTemplateViewSet(BaseCRUD):
    permission_classes = [AllowAny]
    serializer_class = EmailTemplate
    pagination_class = CustomPagination

    _model = EmailTemplateSerializer
    _serializer = serializer_class


class EmailQueueItemSerializerViewSet(BaseCRUD):
    permission_classes = [AllowAny]
    serializer_class = EmailQueueItemSerializer
    pagination_class = CustomPagination

    _model = EmailQueueItem
    _serializer = serializer_class


class EmailLogViewSet(BaseCRUD):
    permission_classes = [AllowAny]
    serializer_class = EmailLogSerializer
    pagination_class = CustomPagination

    _model = EmailLog
    _serializer = serializer_class


class NotificationViewSet(BaseCRUD):
    permission_classes = [AllowAny]
    serializer_class = NotificationSerializer
    pagination_class = CustomPagination

    _model = Notification
    _serializer = serializer_class