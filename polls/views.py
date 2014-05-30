# Create your views here.
#from django.http import HttpResponse
#from polls.models import Poll
from django.template import RequestContext, loader
#from django.http import Http404
#from django.shortcuts import render

#from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render ,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll,ContactForm,Contact 
#from polls.forms import EnterAggreementNo
#from django import forms

def index(request):
    #return HttpResponse('machi this first site index view da  kalakura !!!!!')
    #latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})

#def results(request, poll_id):
#    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

#def vote(request, poll_id):
#    return HttpResponse("you are looking at the vote of %s " % poll_id)

'''from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll'''
# ...

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
   	    try1= Contact.objects.create ( 
		aggreement_no = form.cleaned_data['aggreement_no'],
            	Custid = form.cleaned_data['Custid'],
            	amount = form.cleaned_data['amount'],
            	custname = form.cleaned_data['custname'],
            	mailid = form.cleaned_data['mailid']
		)
	    # recipients = ['info@example.com']
            #if cc_myself:
            # recipients.append(sender)
            #instance = form.save(commit=False)
            #instance.Contact = Contact.objects.all()
            try1.save()
            #from django.core.mail import send_mail
            #send_mail(subject, message, sender, recipients)
	    #form.save()
            return HttpResponseRedirect('/polls/contact') # Redirect after POST

            # return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'polls/contact.html', {
        'form': form,
    })


def thanks(request):
    return render(request, 'polls/thanks.html')


#from django.shortcuts import render_to_response
#from myapp.models import Book

"""def form_view(request):
    if request.method == "POST":
        # the user has submitted the form, see if we have a book
        book_id_form = EnterAggreementNo(request.POST) # instantiate our form class with the user data
        if book_id_form.is_valid():
            # if our form is valid, then we have a book_id that works:
            output = Contact.objects.get(aggreement_no=book_id_form.cleaned_data["aggreement_no"])
            #return render_to_response("polls/fetch.html", { "output": output }, context_instance=RequestContext(request))
	    #render(request, 'polls/fetch.html', {
            #'output': output,
            #'error_message': "You didn't select a choice.",
            #})
	    template = loader.get_template('polls/fetch.html')
            context = RequestContext(request, {'output': output,})
	    return HttpResponse(template.render(context))


        # if the form wasn't valid, it will fall through to the other return statement.
    else:
        # If the user didn't submit a form, instantiate a blank one.
        book_id_form = EnterAggreementNo()
        #return render_to_response("polls/fetch.html", { "book_id_form": book_id_form }, context_instance=RequestContext(request))
        #render(request, 'polls/fetch.html', {
        #    'book_id_form': book_id_form,
        #    'error_message': "You didn't select a choice.",
        #    })
	template = loader.get_template('polls/fetch.html')
        context = RequestContext(request, {'book_id_form': book_id_form,})
        return HttpResponse(template.render(context))

    query = request.GET.get('aggreement_no')
    #try:
    #    query = int (query)
    #except ValueError:
    #    query = None
    #    results = None
    if query != None:
        results = Book.objects.get(aggreement_no=3)
        context = RequestContext(request)
        template = loader.get_template('polls/search.html')
        #context = RequestContext(request)
        return HttpResponse(template.render(context))"""
def search_form(request):
    return render(request, 'polls/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Contact.objects.filter(aggreement_no=q)
        return render(request, 'polls/search_results.html',
            {'books': books, 'query': q})
    else:
        return render(request, 'polls/search_form.html', {'error': True})

def base(request):
    return render(request,'polls/base1.html')
