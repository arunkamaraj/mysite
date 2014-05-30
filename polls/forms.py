from django import forms
from polls.models import Contact

class EnterAggreementNo(forms.Form):
    agno = forms.IntegerField()
# add a custom clean function to validate that the user input
#  is a valid book ID
    def clean_book_id(self):
    	try:
            agno = int(self.cleaned_data["aggreement_no"])
        except:
            agno = None

        if agno and Contact.objects.filter(agno=book_id).count():
      	    return agno
    	else:
            raise forms.ValidationError("Please enter a valid aggreement number.")
