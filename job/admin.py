from django.contrib import admin
from pyjobs.job.models import Job


class JobAdmin(admin.ModelAdmin):
  list_display = ('title','location')
  fields = ('title', 'location')
    
admin.site.register(Job, JobAdmin)

