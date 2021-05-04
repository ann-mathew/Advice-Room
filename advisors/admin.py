from django.contrib import admin
from .models import Advisor

# Register your models here.

class AdvisorModelAdmin(admin.ModelAdmin):
	list_display = ["name", "photo_url", "advisor_id"]           
	
	class Meta:                     
		model = Advisor

admin.site.register(Advisor, AdvisorModelAdmin) 