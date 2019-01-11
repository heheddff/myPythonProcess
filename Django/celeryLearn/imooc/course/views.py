from django.shortcuts import render

from course.tasks import CourseTask

from django.http import HttpResponse
# Create your views here.


def index(request):
    print('start index')
    CourseTask.delay()
    print('end index')
    return HttpResponse('hello celery')