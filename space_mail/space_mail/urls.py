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
from django.urls import path

import mars_client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mars_client.views.index),
    path('new_report/', mars_client.views.new_report, name='new_report'),
    path('sent_reports/', mars_client.views.sent_reports, name='sent_reports'),
    path('pending_reports/', mars_client.views.pending_reports, name='pending_reports')
]
