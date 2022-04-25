from django.contrib import admin

from .models import Client, Class,Membership,Reservation,Instructor
admin.site.register(Client)
admin.site.register(Class)
admin.site.register(Membership)
admin.site.register(Reservation)
admin.site.register(Instructor)