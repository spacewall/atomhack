from django.shortcuts import render, redirect

from mars_client.models import Report

def index(request):
    return redirect('delivered_reports')

def sent_reports(request):
    template = 'delivered.html'
    sorting = request.GET.get('sort')

    if sorting == 'release_date':
        reports = Report.objects.order_by('release_date')
    
    elif sorting == 'send_date':
        reports = Report.objects.order_by('send_date')

    else:
        reports = Report.objects.all()

    context = {'reports': reports}

    return render(request, template, context)
