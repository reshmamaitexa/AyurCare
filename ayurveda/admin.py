from django.contrib import admin
from .models import Log, Patient, Doctor, Doctor_Booking,Remedy, Packages, Medicine

# Register your models here.

admin.site.register(Log)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Doctor_Booking)
admin.site.register(Remedy)
admin.site.register(Packages)
admin.site.register(Medicine)
