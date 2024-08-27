from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ajaxReg', ajaxReg),
    path('suc/<str:token>', sucuser),
    path('ajaxAuth', ajaxAuth),
    path('profile', profile),
    path('chat', chat),
    path('settings', settings),
    path('create_chat', create_chat),
    path('chat/<int:id>', get_chat),
    path('add_user/<int:id_chat>/<int:id_user>', add_user),
    path('settings_chat', settings_chat),
    path('deletemessage/<int:id_message>/<int:id_chat>', deletemessage)
]
