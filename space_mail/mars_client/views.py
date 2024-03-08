from django.shortcuts import render, redirect

from mars_client.models import Report


def new_report(request):
    template = 'new_report/new_report.html'

    name = request.POST.get('name', '')
    text = request.POST.get('text', '')

    return render(request, template)


def index(request):
    return redirect('new_report')


def sent_reports(request):
    template = 'sent/sent.html'

    context = {'reports': Report.objects.all()}

    return render(request, template, context)


def pending_reports(request):
    template = 'waiting/waiting.html'

    context = {'reports': Report.objects.all()}

    return render(request, template, context)
