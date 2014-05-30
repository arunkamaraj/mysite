from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView,DayArchiveView
from search import views
# i m commanding the below line because we are seperated the url to arun_dj
#from arun_dj.views import EntryArchiveIndexView
#from arun_dj.models import Entry
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls',namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),

    #we are used as weblog now we can changed to blog
    #This is used for Entry
    url(r'^blog/',include('arun_dj.urls.entries')),

    #This is for category
    url(r'^blog/category/',include('arun_dj.urls.categories')),

    #This is for link
    url(r'^blog/link/',include('arun_dj.urls.links')),

    #This is for tag
    url(r'^blog/tag/',include('arun_dj.urls.tags')),

    #url(r'^first-page/',include('django.contrib.flatpages.urls')),
    url(r'^tinymce/(?P<path>.*)$','django.views.static.serve',{'document_root': '/home/ak/Downloads/tinymce/js/tinymce/'}),

    #for search 
    url(r'^search/','search.views.search'),				

    #for flatpage	
    url(r'', include('django.contrib.flatpages.urls')),
)
