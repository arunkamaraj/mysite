# Create your views here.
#while inporting the beliw module i have mulpitple reeoe in crib  and FlatPage
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,Context
from django.contrib.flatpages.models import FlatPage 
from django.shortcuts import render_to_response
from search.models import SearchKeyword
''' 
def search(request):
    query=request.GET['q']
    result=FlatPage.objects.filter(content__icontains=query)
    template=loader.get_template('search/search.html')
    context=Context({'query':query,'result':result})
    response=template.render(context)
    return HttpResponse(response)
'''    
def search(request):
	query=request.GET.get('q','')
	result=[]
	kw_result=[]
	if query:
    	
#       query=request.GET['q']
#    	return render_to_response('search/search.html',{'query':request.GET['q'],'result':FlatPage.objects.filter(content__icontains=request.GET['q'])})
		kw_result=FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
		if kw_result.count()==1 :
			return HttpResponseRedirect(kw_result[0].get_absolute_url())
#	kw_result=SearchKeyword.objects.filter(keyword__in=query.split()).distinct()
#       kw_result=SearchKeyword.objects.filter(keyword__in =[u'first']).distinct()
		result =FlatPage.objects.filter(content__icontains=query)
		return render_to_response('search/search1.html',{'query':query,'result':result,'kw_result':kw_result})
'''
def search(request):
	query = request.GET.get('q', '')
	keyword_results = []
	results = []
	if query:
		keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
		results = FlatPage.objects.filter(content__icontains=query)
		return render_to_response('search/search.html',{ 'query': query,'keyword_results': keyword_results,'results': results })

'''
