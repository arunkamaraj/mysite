from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class Poll_admin(admin.ModelAdmin):
    fieldsets=[
        ('Question area',{'fields':['question']}),
        ('Date and time information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    list_display = ('question', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]
admin.site.register(Choice)
admin.site.register(Poll,Poll_admin)
