from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os


def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    # PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
    })

def health(request):
    return HttpResponse(PageView.objects.count())
