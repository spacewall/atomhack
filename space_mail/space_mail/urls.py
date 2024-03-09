"""
URL configuration for space_mail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from mars_client.views import index, sent_reports, pending_reports, NewReportCreateView

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('new_report/', NewReportCreateView.as_view(), name='new_report'),
    path('sent_reports/', sent_reports, name='sent_reports'),
    path('pending_reports/', pending_reports, name='pending_reports'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file")
]
