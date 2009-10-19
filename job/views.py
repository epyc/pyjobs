# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world. You're at the jobs index.")

def job_detail(request, job_id):
  print job_id
  return render_to_response('job/detail.html', {'job_id':job_id})

