from django.urls import path

from core.views import LetsBeFriends


app_name  = 'core'


urlpatterns = [
    path('', LetsBeFriends.as_view(), name='hello'),
]