from django.urls import path, include

from mars_client.views import index, sent_reports, pending_reports, NewReportCreateView

urlpatterns = [
    path('', index, name='mars_base'),
    path('new_report/', NewReportCreateView.as_view(), name='new_report'),
    path('sent_reports/', sent_reports, name='sent_reports'),
    path('pending_reports/', pending_reports, name='pending_reports'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file")
]
