from django.contrib import admin
from .models import Log, Patient, Doctor, Doctor_Booking,Remedy, Packages, Medicine, Review, Complaints, Complaints_Replay, ComplaintsAndReplay, Token_Booking, Package_Book, Package_payments, Medicine_Carts_tb, Medicine_order_tb

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
admin.site.register(Package_Book)
admin.site.register(Package_payments)
admin.site.register(Medicine_Carts_tb)
admin.site.register(Medicine_order_tb)
