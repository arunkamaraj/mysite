from django.conf.urls import patterns,url
from polls import views

urlpatterns=patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    # ex: /polls/contact/
    url(r'^contact/',views.contact,name='contact'),
    #thanks
    url(r'^thanks/',views.thanks,name='thanks'),
    #fetch
#    url(r'^fetch/',views.form_view,name='form_view'),
    #home
    #http://127.0.0.1:8000/polls/base/
    url(r'^base/',views.base,name='base'),
    #http://127.0.0.1:8000/polls/search_form/
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
)	
