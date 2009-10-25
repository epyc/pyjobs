# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from pyjobs.job import models

def index(request, city):
  if city:
    _jobs = models.Job.objects.filter(location = city)
  else:
    _jobs = models.Job.objects.all()
  return render_to_response('job/list.html', {'jobs': _jobs, 'cities':['montreal','sfbay'],'city': city},)


def job_detail(request, job_id):
  _job = models.Job.objects.get(id=job_id)
  return render_to_response('job/detail.html', {'job':_job})


