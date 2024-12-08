from django.contrib import admin
from careproapp.models import Appointment, Message, member


# Register your models here.
admin.site.register(Appointment)
admin.site.register(Message)
admin.site.register(member)