from django.contrib import admin
from .models import Log, Patient, Doctor, Doctor_Booking,Remedy, Packages, Medicine, Review, Complaints, Complaints_Replay, ComplaintsAndReplay, Token_Booking, Package_Books, Package_payment_tb, Treatments

# Register your models here.

admin.site.register(Log)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Doctor_Booking)
admin.site.register(Remedy)
admin.site.register(Packages)
admin.site.register(Medicine)
admin.site.register(Review)
admin.site.register(Complaints)
admin.site.register(Complaints_Replay)
admin.site.register(ComplaintsAndReplay)
admin.site.register(Token_Booking)
admin.site.register(Package_Books)
admin.site.register(Package_payment_tb)
admin.site.register(Treatments)
