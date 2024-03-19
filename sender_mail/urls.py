from django.urls import path
from .views import (
    EmailTemplateViewSet, EmailQueueItemSerializerViewSet, EmailLogViewSet,
    NotificationViewSet
)

urlpatterns = [
    path('email/template/', EmailTemplateViewSet.as_view({'get': 'lists'})),
    path('email/template/<str:id>/', EmailTemplateViewSet.as_view({'get': 'get'})),
    
    path('email/queue/', EmailQueueItemSerializerViewSet.as_view({'get': 'lists'})),
    path('email/queue/<str:id>/', EmailQueueItemSerializerViewSet.as_view({'get': 'get', 'put': 'update'})),
    
    path('email/logs/', EmailLogViewSet.as_view({'get': 'lists'})),
    path('email/log/<str:id>/', EmailLogViewSet.as_view({'get': 'get'})),

    path('email/notifications/', NotificationViewSet.as_view({'get': 'lists'})),
    path('email/notification/<str:id>/', NotificationViewSet.as_view({'get': 'get'})),
]