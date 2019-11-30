from django.urls import path

from .views import UserView, MessageView

urlpatterns = [
    path('accounts/', UserView.as_view()),
    path('messages/', MessageView.as_view())
]