from django.contrib import admin
from search.models import SearchKeyword
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

#it is for summa we ll see the exact function later
"""class SearchKeywordAdmin(admin.ModelAdmin):
	pass
admin.site.register(SearchKeyword,SearchKeywordAdmin)"""
class SearchKeywordInline(admin.StackedInline):
	model=SearchKeyword

class FlatPageWithSearchKeyword(FlatPageAdmin):
	inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage,FlatPageWithSearchKeyword)

