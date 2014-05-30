from django.db import models
from django.utils import timezone
import datetime
from django import forms

# Create your models here.
class Poll(models.Model):
    def __unicode__(self):
        return self.question
    def is_recently(self):
        return self.pub_date > timezone.now()-datetime.timedelta(days=1)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    
    def __unicode__(self):
        return self.choice_text
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Contact(models.Model):
    def __unicode__(self):
	return '%s' % self.aggreement_no
    aggreement_no = models.IntegerField(default=0)
    Custid = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    custname = models.CharField(max_length=200)
    mailid = models.EmailField()


class ContactForm(forms.Form):
    #subject = forms.CharField(max_length=100)
    #message = forms.CharField()
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)
    aggreement_no = forms.IntegerField()
    Custid = forms.IntegerField()
    amount = forms.IntegerField()
    custname = forms.CharField(max_length=200)
    mailid = forms.EmailField()
