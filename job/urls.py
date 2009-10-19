from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'$/', 'pyjobs.job.views.index'),
    (r'(?P<job_id>\d+)', 'pyjobs.job.views.job_detail')
)

