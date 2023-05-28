from django.db import models

# Create your models here.

class Log(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10)
    def __str__(self):
        return self.username    

class Patient(models.Model):
    patientname = models.CharField(max_length = 20)
    patientage = models.CharField(max_length = 20)
    patientgender = models.CharField(max_length = 20)
    patientemail = models.EmailField(max_length = 20)
    patientphone = models.CharField(max_length = 20)
    patientaddress = models.CharField(max_length=50)
    patientplace = models.CharField(max_length=20)
    patientpost = models.CharField(max_length=20)
    patientpincode = models.CharField(max_length=20)
    log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    patientstatus = models.CharField(max_length=10)

    def __str__(self):
        return self.patientname

class Doctor(models.Model):
    doctorname = models.CharField(max_length = 20)
    doctorqualification = models.CharField(max_length = 20)
    doctorexperience = models.CharField(max_length = 20)
    doctoremail = models.EmailField(max_length = 20)
    doctorphone = models.CharField(max_length = 20)
    doctorspecialization = models.CharField(max_length=50)
    doctorgender = models.CharField(max_length=20)  
    doctor_available_days = models.CharField(max_length=40)
    doctor_available_time = models.CharField(max_length=40)
    doctorprofile_photo = models.ImageField(upload_to='images')
    log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    doctorstatus = models.CharField(max_length=10)

    def __str__(self):
        return self.doctorname


class Doctor_Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_day = models.CharField(max_length=40)
    appointment_time = models.CharField(max_length=40)
    bookingstatus = models.CharField(max_length=10)

    def __str__(self):
        return self.appointment_day


class Remedy(models.Model):
    disease = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=500)
    remedy = models.CharField(max_length=500)
    remedy_photo = models.ImageField(upload_to='images')
    remedystatus = models.CharField(max_length=10)

    def __str__(self):
        return self.disease


class Packages(models.Model):
    package_name = models.CharField(max_length=50)
    package_goal = models.CharField(max_length=500)
    package_description = models.CharField(max_length=500)
    package_duration = models.CharField(max_length=50)
    package_price = models.CharField(max_length=50)
    package_photo = models.ImageField(upload_to='images')
    package_status = models.CharField(max_length=10)

    def __str__(self):
        return self.package_name


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=50)
    medicine_qnty = models.CharField(max_length=50)
    medicine_description = models.CharField(max_length=500)
    medicine_dosage = models.CharField(max_length=500)
    medicine_usage = models.CharField(max_length=500)
    medicine_price = models.CharField(max_length=50)
    medicine_photo = models.ImageField(upload_to='images')
    medicine_status = models.CharField(max_length=10)

    def __str__(self):
        return self.medicine_name


class Review(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)
    date = models.DateField()
    review_status = models.CharField(max_length=10)

    def __str__(self):
        return self.feedback


class Complaints(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    complaint_status = models.CharField(max_length=10)

    def __str__(self):
        return self.complaint

class Complaints_Replay(models.Model):
    patient = models.CharField(max_length=50)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    replay= models.CharField(max_length=500,default='No Replay')
    complaint_status = models.CharField(max_length=10)

    def __str__(self):
        return self.replay


class ComplaintsAndReplay(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    replay= models.CharField(max_length=500,default='No Replay')
    complaint_status = models.CharField(max_length=10)

    def __str__(self):
        return self.complaint


class Token_Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.CharField(max_length=40)
    appointment_time = models.CharField(max_length=40)
    number = models.IntegerField(default=0)
    bookingstatus = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.doctor



# class Package_Booking(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     packages=models.ForeignKey(Packages,on_delete=models.CASCADE)
#     package_name = models.CharField(max_length=500)
#     package_duration = models.CharField(max_length=500)
#     package_price= models.CharField(max_length=500)
#     booking_date = models.DateField()
#     booking_status = models.CharField(max_length=10)
#     package_photo = models.ImageField(upload_to='images')


class Package_Book(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    packages=models.ForeignKey(Packages,on_delete=models.CASCADE)
    package_name = models.CharField(max_length=500)
    package_duration = models.CharField(max_length=500)
    package_price= models.CharField(max_length=500)
    booking_date = models.DateField()
    booking_status = models.CharField(max_length=10)
    package_photo = models.ImageField(upload_to='images')


class Package_payments(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=50,blank=True, null=True)
    package_booking=models.ForeignKey(Package_Book,on_delete=models.CASCADE)
    package_name=models.CharField(max_length=50,blank=True, null=True)
    package_price= models.IntegerField()
    payment_status = models.CharField(max_length=10,blank=True, null=True)



class Medicine_Carts_tb(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=500)
    medicine_qnty = models.CharField(max_length=500)
    medicine_price= models.CharField(max_length=500)
    cart_status = models.CharField(max_length=10)
    medicine_photo = models.ImageField(upload_to='images')



class Medicine_order_tb(models.Model):
    user=models.ForeignKey(Patient,on_delete=models.CASCADE)
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=500, blank=True, null=True)
    medicine_qnty = models.CharField(max_length=500,blank=True, null=True)
    medicine_price= models.IntegerField()
    medicine_photo = models.ImageField(upload_to='images', blank=True, null=True)
    order_status = models.CharField(max_length=10,blank=True, null=True)