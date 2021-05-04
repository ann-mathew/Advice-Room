from django.contrib import admin
from .models import Booking

# Register your models here.

class BookingModelAdmin(admin.ModelAdmin):
	list_display = ["user_id", "advisor_id", "booking_id", "booking_time"]           
	
	class Meta:                     
		model = Booking

admin.site.register(Booking, BookingModelAdmin) 