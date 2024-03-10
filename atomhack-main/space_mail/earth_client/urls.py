from django.urls import path

from earth_client.views import index, sent_reports

urlpatterns = [
    path('', index, name='earth_base'),
    path('sent_reports/', sent_reports, name='delivered_reports')
]
