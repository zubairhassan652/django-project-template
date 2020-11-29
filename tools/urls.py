import debug_toolbar
from django.urls import path, include
from .views import hello_view, TestEmailView

from django.apps import apps

for app in apps.get_app_configs():
    app_name = app.name

urlpatterns = [  
    path('',  hello_view, name='hello'),
    path('test-email/<str:email_id>', TestEmailView.as_view(), name="test_email")
]