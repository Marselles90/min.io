from django.urls import path, include
from accounts.urls import urlpatterns as accounts_app_urls
from sender_mail.urls import urlpatterns as send_mail_urls

urlpatterns = [
    path('', include(accounts_app_urls)),
    path('', include(send_mail_urls)),
]