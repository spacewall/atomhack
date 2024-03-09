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
    sorting = request.GET.get('sort')
    filtering = request.GET.get('filter')

    if sorting == 'release_date':
        reports = Report.objects.order_by('release_date')
    
    elif sorting == 'send_date':
        reports = Report.objects.order_by('send_date')

    else:
        reports = Report.objects.all()

    context = {'reports': reports}

    return render(request, template, context)

def pending_reports(request):
    template = 'pending.html'
    sorting = request.GET.get('sort')
    filtering = request.GET.get('filter')

    if sorting == 'release_date':
        reports = Report.objects.order_by('release_date')

    else:
        reports = Report.objects.all()

    context = {'reports': Report.objects.all()}

    return render(request, template, context)
