from BeautifulSoup import BeautifulSoup
import urllib2
import re
from pyjobs.job import models
import datetime

craigslist_base = "http://%s.craigslist.org" 
query = "/search/sof?query=python&catAbbreviation=sof"

def crawl_cl(city):
  url = (craigslist_base + query) % city
  data = urllib2.urlopen(url)
  soup = BeautifulSoup( data.read() )
  
  for job in soup.findAll('a', attrs={'href': re.compile(".*/sof/[0-9]*.html")}):
     
     job_url = CRAIGSLIST_BASE + job['href']
     job_post_data = urllib2.urlopen(job_url).read()
     job_soup = BeautifulSoup(job_post_data)

     body = job_soup.find('div', {"id":"userbody"})
     title = strip_tags(unicode(job_soup.find('h2')))
     date_added = clget_date(job_soup) 

     newjob = models.Job(title = title, content = body, location = city, date_added = date_added)
     newjob.save()


def clget_date(job_soup):
  f = unicode(job_soup).find('Date:')
  date_added = re.compile("Date: (.*)\<br.*>").match(unicode(job_soup)[f:f+50]).groups()[0]
  d = datetime.datetime.strptime(date_added.rstrip()[:10], '%Y-%m-%d')
  return date_added
  

def strip_tags(value):
    "Return the given HTML with all tags stripped."
    return re.sub(r'<[^>]*?>', '', value) 

if __name__=='__main__':
  crawl_cl('montreal')
  crawl_cl('sfbay')


