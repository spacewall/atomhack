from django.shortcuts import render, redirect
from django.views.generic import CreateView

from mars_client.models import Report

class NewReportCreateView(CreateView):
    model = Report
    template_name = 'new_report.html'

    fields = ['name', 'author', 'context', 'files']


def index(request):
    return redirect('new_report')

def sent_reports(request):
    template = 'sent.html'

    context = {'reports': Report.objects.all()}

    return render(request, template, context)

def pending_reports(request):
    template = 'pending.html'

    context = {'reports': Report.objects.all()}

    return render(request, template, context)
