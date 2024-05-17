from django.urls import path
from .views import SendContactsView

urlpatterns = [
    path('send_email/', SendContactsView.as_view()),
]
