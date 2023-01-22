from django.contrib import admin
from .models import Appointment
# Register your models here.

class AdminAppointment(admin.ModelAdmin):
    list_display = ('id', 'user', 'date','time')
    list_filter = ('date', )
    search_fields = ('user', )
    list_per_page = 25

admin.site.register(Appointment, AdminAppointment)