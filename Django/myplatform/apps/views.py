from django.shortcuts import render
from .tasks import func
from django.http import HttpResponse
# Create your views here.


def index(request):
    print('start index')
    func.delay()
    print('end index')
    return HttpResponse('hello celery')
