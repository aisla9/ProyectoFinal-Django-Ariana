from django.urls import path
from .views import InboxView, SendMessageView

urlpatterns = [
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('enviar/', SendMessageView.as_view(), name='send_message'),
]