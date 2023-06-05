from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.conf import settings
from django.db.models import Sum
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Log, Patient, Doctor, Doctor_Booking, Remedy, Packages, Medicine, Review, Complaints, Complaints_Replay, ComplaintsAndReplay, Token_Booking, Package_Books, Package_payment_tb, Treatments, Cart, order, payment
from ayurveda.serializers import LoginUsersSerializer, PatientRegisterSerializer, doctorRegisterSerializer, DoctorBookingSerializer, RemedySerializer, PackageSerializer, MedicineSerializer, ReviewSerializer, ComplaintsSerializer, ComplaintReplaySerializer, ComplaintsAndReplaySerializer, DoctorTokenBookingSerializer, PackageBookingSerializer, Package_PaymentSerializer, TreatmentSerializer, CartSerializer, OrderSerializer, PaymentSerializer
from django.db.models import Q


# Create your views here.


# ------------------------------------------------ patient registration ------------------------------------------------


class PatientRegisterAPIView(GenericAPIView):
    serializer_class = PatientRegisterSerializer
    serializer_class_login = LoginUsersSerializer

    def post(self, request):
        
        login_id=''
        patientname = request.data.get('patientname')
        patientage = request.data.get('patientage')
        patientgender = request.data.get('patientgender')
        patientemail = request.data.get('patientemail')
        patientphone = request.data.get('patientphone')
        patientaddress = request.data.get('patientaddress')
        patientplace = request.data.get('patientplace')
        patientpost = request.data.get('patientpost')
        patientpincode = request.data.get('patientpincode')
        patientusername = request.data.get('patientusername')
        patientpassword = request.data.get('patientpassword')
        role = 'patient'
        patientstatus = '0'


        if (Log.objects.filter(username=patientusername)):
            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data = {'username': patientusername, 'password':patientpassword, 'role':role})

        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id = log.id
            print(login_id)
        serializer = self.serializer_class(data= {'patientname':patientname, 'patientage':patientage,'patientgender':patientgender, 'patientemail':patientemail, 'patientphone':patientphone, 'patientaddress':patientaddress, 'patientplace':patientplace, 'patientpost':patientpost,'patientpincode':patientpincode,'log_id':login_id, 'patientstatus':patientstatus,'role':role})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data, 'message':'Patient registered successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------ doctor registration ------------------------------------------------


class DoctorRegisterAPIView(GenericAPIView):
    serializer_class = doctorRegisterSerializer
    serializer_class_login = LoginUsersSerializer

    def post(self, request):
        
        login_id=''
        doctorname = request.data.get('doctorname')
        doctorqualification = request.data.get('doctorqualification')
        doctorexperience = request.data.get('doctorexperience')
        doctoremail = request.data.get('doctoremail')
        doctorphone = request.data.get('doctorphone')
        doctorspecialization = request.data.get('doctorspecialization')
        doctorgender = request.data.get('doctorgender')
        doctor_available_days = request.data.get('doctor_available_days')
        doctor_available_time = request.data.get('doctor_available_time')
        doctorprofile_photo = request.data.get('doctorprofile_photo')
        doctorusername = request.data.get('doctorusername')
        doctorpassword = request.data.get('doctorpassword')
        role = 'doctor'
        doctorstatus = '1'


        if (Log.objects.filter(username=doctorusername)):
            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data = {'username': doctorusername, 'password':doctorpassword, 'role':role})

        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id = log.id
            print(login_id)
        serializer = self.serializer_class(data= {'doctorname':doctorname, 'doctorqualification':doctorqualification,'doctorexperience':doctorexperience, 'doctoremail':doctoremail, 'doctorphone':doctorphone, 'doctorspecialization':doctorspecialization, 'doctorgender':doctorgender, 'doctor_available_days':doctor_available_days, 'doctor_available_time':doctor_available_time, 'doctorprofile_photo':doctorprofile_photo,'log_id':login_id, 'doctorstatus':doctorstatus,'role':role})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data, 'message':'Doctor registered successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------ user login ------------------------------------------------

class LoginUsersAPIView(GenericAPIView):
    serializer_class = LoginUsersSerializer

    def post(self, request):
        u_id=''
        username = request.data.get('username')
        password = request.data.get('password')
        # role = request.data.get('role')
        logreg = Log.objects.filter(username=username, password=password)
        if (logreg.count()>0):
            read_serializer = LoginUsersSerializer(logreg, many=True)
            for i in read_serializer.data:
                id = i['id']
                print(id)
                role = i['role']
                regdata=Patient.objects.all().filter(log_id=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status=i['patientstatus']
                     print(u_id)
                regdata=Doctor.objects.all().filter(log_id=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status = i['doctorstatus']
                     print(l_status)
                     print(u_id)
                
            return Response({'data':{'login_id':id,'username':username,'password':password,'role':role,'user_id':u_id,'l_status':l_status},'success': True, 'message':'Logged in successfully'}, status=status.HTTP_200_OK)       
        else:
            return Response({'data':'username or password is invalid', 'success': False, }, status = status.HTTP_400_BAD_REQUEST)



# ------------------------------------------------ patient all and single view, edit, delete ------------------------------------------------

class Get_PatientAPIView(GenericAPIView):
    serializer_class = PatientRegisterSerializer
    def get(self, request):
        queryset = Patient.objects.all()
        if (queryset.count()>0):
            serializer = PatientRegisterSerializer(queryset, many=True)
            # for i in serializer.data: 
                # login_id = i['log_id']
                # name = i['name']
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class SinglePatientAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Patient.objects.get(pk=id)
        serializer =PatientRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single patient data', 'success':True}, status=status.HTTP_200_OK)



class Update_PatientAPIView(GenericAPIView):
    serializer_class = PatientRegisterSerializer
    def put(self, request, id):
        queryset = Patient.objects.get(pk=id)
        print(queryset)
        serializer = PatientRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
            


class Delete_PatientAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Log.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully',  'success':True}, status=status.HTTP_200_OK)



# ------------------------------------------------ doctor all and single view, edit, delete ------------------------------------------------

class Get_DoctorAPIView(GenericAPIView):
    serializer_class = doctorRegisterSerializer
    def get(self, request):
        queryset = Doctor.objects.all()
        if (queryset.count()>0):
            serializer = doctorRegisterSerializer(queryset, many=True)
            # for i in serializer.data: 
                # login_id = i['log_id']
                # name = i['name']
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class SingleDoctorAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Doctor.objects.get(pk=id)
        serializer =doctorRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single Doctor data', 'success':True}, status=status.HTTP_200_OK)

        

class Update_DoctorAPIView(GenericAPIView):
    serializer_class = doctorRegisterSerializer
    def put(self, request, id):
        queryset = Doctor.objects.get(pk=id)
        print(queryset)
        serializer = doctorRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':1}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
            


class Delete_DoctorAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Log.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)



# ------------------------------------------------------ admin approve patient and approve ----------------------------------------------


class AdminApprove_PatientAPIView(GenericAPIView):
    def post(self, request, id):
        serializer_class = PatientRegisterSerializer
        user = Patient.objects.get(pk=id)
        user.patientstatus = 1
        user.save()
        serializer = serializer_class(user)
        return Response({'data':serializer.data,'message':'Admin Approved Patient', 'success':True}, status=status.HTTP_200_OK)


class AdminApprove_DoctorAPIView(GenericAPIView):
    def post(self, request, id):
        serializer_class = doctorRegisterSerializer
        user = Doctor.objects.get(pk=id)
        user.doctorstatus = 1
        user.save()
        serializer = serializer_class(user)
        return Response({'data':serializer.data,'message':'Doctor Approved', 'success':True}, status=status.HTTP_200_OK)


# ----------------------------------- patient book doctor -----------------------------------------------------------------


class PatientBookDoctorAPIView(GenericAPIView):
    serializer_class = DoctorBookingSerializer

    def post(self, request):
        doctor = request.data.get('doctor')
        patient = request.data.get('patient')
        appointment_day = request.data.get('appointment_day')
        appointment_time = request.data.get('appointment_time')
        bookingstatus = request.data.get('bookingstatus')


        serializer = self.serializer_class(data= {'doctor':doctor, 'patient':patient,'appointment_day':appointment_day,'appointment_time':appointment_time,'bookingstatus':bookingstatus})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Doctor Booked successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------ patient search doctor --------------------------------------------------
class PatientSearchDoctorAPIView(GenericAPIView):
    def post(self,request):
        query = request.data.get('query')
        print(query)
        
        i = Doctor.objects.filter(doctorspecialization__icontains=query) or Doctor.objects.filter(doctor_available_days__icontains=query)
        for dta in i:
            print(dta)
        

        data = [{'doctorname':info.doctorname,'doctoremail':info.doctoremail, 'doctorphone':info.doctorphone, 'doctorspecialization':info.doctorspecialization, 'doctorgender':info.doctorgender, 'doctor_available_days':info.doctor_available_days, 'doctor_available_time':info.doctor_available_time}
                for info in i]
        return Response({'data':data, 'message':'Successfully fetched', 'success':True}, status=status.HTTP_200_OK)


# ------------------------------------------------- Admin view all doctor bookings ---------------------------------------------


class Get_DoctorBookingAPIView(GenericAPIView):
    serializer_class = DoctorBookingSerializer
    def get(self, request):
        queryset = Doctor_Booking.objects.all()
        if (queryset.count()>0):
            serializer = DoctorBookingSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Doctor booking all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------------------- Doctor View Booking Data -----------------------------------------------------


class ViewDoctorBookingAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Doctor_Booking.objects.all().filter(doctor=id).values()
        # print(queryset)
        # serializer =DoctorBookingSerializer(queryset)
        return Response({'data': queryset, 'message':' Doctor Booking  data', 'success':True}, status=status.HTTP_200_OK)



# ----------------------------------------- User View Remedy Data -----------------------------------------------------

class Get_RemedyAPIView(GenericAPIView):
    serializer_class = RemedySerializer
    def get(self, request):
        queryset = Remedy.objects.all()
        if (queryset.count()>0):
            serializer = RemedySerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Remedy all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleRemedyAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Remedy.objects.get(pk=id)
        serializer =RemedySerializer(queryset)
        return Response({'data': serializer.data, 'message':'single remedy data', 'success':True}, status=status.HTTP_200_OK)

# ----------------------------------------- User View Package Data -----------------------------------------------------


class Get_PackageAPIView(GenericAPIView):
    serializer_class = PackageSerializer
    def get(self, request):
        queryset = Packages.objects.all()
        if (queryset.count()>0):
            serializer = PackageSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Package all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SinglePackageAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Packages.objects.get(pk=id)
        serializer =PackageSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single package data', 'success':True}, status=status.HTTP_200_OK)


# ----------------------------------------- User View Medicine Data -----------------------------------------------------


class Get_MedicineAPIView(GenericAPIView):
    serializer_class = MedicineSerializer
    def get(self, request):
        queryset = Medicine.objects.all()
        if (queryset.count()>0):
            serializer = MedicineSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Medicine all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleMedicineAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Medicine.objects.get(pk=id)
        serializer =MedicineSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single medicine data', 'success':True}, status=status.HTTP_200_OK)



# ----------------------------------------- Patient add review and single view and all review -----------------------------------------------------

class PatientReviewAPIView(GenericAPIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        patient = request.data.get('patient')
        feedback = request.data.get('feedback')
        rating = request.data.get('rating')
        date = request.data.get('date')
        review_status="0"


        serializer = self.serializer_class(data= {'patient':patient, 'feedback':feedback,'rating':rating,'date':date,'review_status':review_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Review Added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleReviewAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Patient.objects.all().filter(pk=id).values()
        for i in queryset:
            patient_id=i['id']
        data=Review.objects.get(patient=patient_id)
        serializer =ReviewSerializer(data)
        return Response({'data': serializer.data, 'message':'single Review data', 'success':True}, status=status.HTTP_200_OK)


class Get_ReviewAPIView(GenericAPIView):
    serializer_class = ReviewSerializer
    def get(self, request):
        queryset = Review.objects.all()
        if (queryset.count()>0):
            serializer = ReviewSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Review all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------------------- Patient post complaints and view complaints replay-----------------------------------------------------

# class PatientComplaintsAPIView(GenericAPIView):
#     serializer_class = ComplaintReplaySerializer

#     def post(self, request):
#         patient = request.data.get('patient')
#         complaint = request.data.get('complaint')
#         date = request.data.get('date')
#         complaint_status="0"


#         serializer = self.serializer_class(data= {'patient':patient, 'complaint':complaint,'date':date,'complaint_status':complaint_status})
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data, 'message':'Complaints Added successfully', 'success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



class PatientComplaintsAndReplayAPIView(GenericAPIView):
    serializer_class = ComplaintsAndReplaySerializer

    def post(self, request):
        patient = request.data.get('patient')
        complaint = request.data.get('complaint')
        date = request.data.get('date')
        complaint_status="0"


        serializer = self.serializer_class(data= {'patient':patient, 'complaint':complaint,'date':date,'complaint_status':complaint_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Complaints Added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



# class ComplaintAndReplayPIView(GenericAPIView):
#     def get(self, request, id):
#         queryset = Patient.objects.all().filter(pk=id).values()
#         print(queryset)
#         for i in queryset:
#             patient=i['id']
#             print('///////////',patient)
#         data=ComplaintsAndReplay.objects.get(patient=patient)
#         serializer =ComplaintsAndReplaySerializer(data)
#         return Response({'data': serializer.data, 'message':'complaint  data', 'success':True}, status=status.HTTP_200_OK)

class ComplaintAndReplayPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Patient.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            patient = i['id']
            print('///////////',patient)
        instance = ComplaintsAndReplay.objects.get(patient=patient)
        print("======",instance)
        serializer = ComplaintsAndReplaySerializer(instance)
        return Response({'data': serializer.data, 'message':'complaint  data', 'success':True}, status=status.HTTP_200_OK)

# class ComplaintReplayPIView(GenericAPIView):
#     def get(self, request, id):
#         queryset = Patient.objects.all().filter(pk=id).values()
#         for i in queryset:
#             patient_id=i['patientname']
#         data=Complaints_Replay.objects.get(patient=patient_id)
#         serializer =ComplaintReplaySerializer(data)
#         return Response({'data': serializer.data, 'message':'complaint replay data', 'success':True}, status=status.HTTP_200_OK)

# ----------------------------------------- Get Image Data -----------------------------------------------------

# class Get_ImageAPIView(GenericAPIView):
#     def get(self, request,pk):
#         my_model = get_object_or_404(Packages, pk=pk)
#         image_base64 = my_model.package_photo
#         return Response({'data': image_base64, 'message':'Image data', 'success':True}, status=status.HTTP_200_OK)
#         # else:
#         #     return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------------------- Patient Book Doctor/Doctor view Booking Data/Patient View Booking Data -----------------------------------------------------


class PatientBookDoctorTokenAPIView(GenericAPIView):
    serializer_class = DoctorTokenBookingSerializer

    def post(self, request):
        doctor = request.data.get('doctor')
        patient = request.data.get('patient')
        appointment_date = request.data.get('appointment_date')
        appointment_time = request.data.get('appointment_time')
        bookingstatus = "0"

        last_token = Token_Booking.objects.all().filter(Q(doctor=doctor) & Q(appointment_date=appointment_date)).values()
        print(last_token)
        if last_token:
            for i in last_token:
                num=i['number']
                number = num + 1
        else:
            number = 1
        serializer = self.serializer_class(data= {'doctor':doctor, 'patient':patient,'appointment_date':appointment_date,'appointment_time':appointment_time,'bookingstatus':bookingstatus,'number':number})
        
        # last_token = Token_Booking.objects.order_by('-created_at').first()
        # if last_token:
        #     number = last_token.number + 1
        # else:
        #     number = 1
        # token = self.serializer_class(data={'number':number})
        # serializer = DoctorTokenBookingSerializer(token)

        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Doctor Booked successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)




class DoctorTokenAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Doctor.objects.filter(pk=id).values()
        doctors = []
        for i in queryset:
            doctor = i['id']
            doctors.append(doctor)
            print('///////////', doctor)
        
        booking_data = []
        instances = Token_Booking.objects.filter(doctor__in=doctors).values()
        for instance in instances:
            book_id = instance["id"]
            doctor = instance["doctor_id"]
            patient = instance["patient_id"]
            appointment_date = instance["appointment_date"]
            appointment_time = instance["appointment_time"]
            number = instance["number"]
            bookingstatus = instance["bookingstatus"]
            a= Patient.objects.all().filter(id=patient).values()

            for i in a:
                patient_name=i["patientname"]

            booking_data.append({
                "book_id": book_id,
                "doctor": doctor,
                "patient": patient,
                "appointment_date": appointment_date,
                "appointment_time": appointment_time,
                "number": number,
                "bookingstatus": bookingstatus,
                "patientname": patient_name

            })

        return Response({
            'data': booking_data,
            'message': 'Doctor Booking data',
            'success': True
        }, status=status.HTTP_200_OK)






class PatientTokenAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = Patient.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            patient = i['id']
            print('///////////',patient)
        instance = Token_Booking.objects.all().filter(patient=patient).values()
        print("======",instance)
        # serializer = DoctorTokenBookingSerializer(instance)
        return Response({'data': instance, 'message':'Patient Booking  data', 'success':True}, status=status.HTTP_200_OK)


class Get_AllBookingAPIView(GenericAPIView):
    serializer_class = DoctorTokenBookingSerializer
    def get(self, request):
        queryset = Token_Booking.objects.all()
        if (queryset.count()>0):
            serializer = DoctorTokenBookingSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Booking all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)





class PackageBookingAPIView(GenericAPIView):
    serializer_class = PackageBookingSerializer

    def post(self, request):
       

        
        patient = request.data.get('patient')
        packages=request.data.get('packages')
        booking_date=request.data.get('booking_date')
        booking_status="0"
       
       
        data=Packages.objects.all().filter(id=packages).values()
        for i in data:
            print(i)
            package_name=i['package_name']
            package_duration=i['package_duration']
            package_price=i['package_price']
            price=int(package_price)
            print(price)

        p_info = Packages.objects.get(id=packages)
        package_photo = p_info.package_photo
        print(package_photo)
            

        serializer = self.serializer_class(data= {'patient':patient,'packages':packages,'package_name':package_name,'booking_date':booking_date,'package_duration':package_duration,'booking_status':booking_status,'package_price':price,'package_photo':package_photo})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Package Booked successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)



class PackageSingleBookingAPIView(GenericAPIView):
    
    def get(self, request, id):
        u_id=""
        qset = Patient.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']

        data = Package_Books.objects.filter(patient=u_id).values()
        serialized_data = list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['package_photo'] = settings.MEDIA_URL + str(obj['package_photo'])
        return Response({'data':serialized_data, 'message':'single product data', 'success':True}, status=status.HTTP_200_OK)



class BookingAllPriceAPIView(GenericAPIView):

    def get(self, request,id):
        book = Package_Books.objects.filter(patient=id)
        print(book)

        tot = book.aggregate(total=Sum('package_price'))['total']
        print(tot)
        return Response({'data':{ 'total_price':tot} , 'message': 'Get Total Booking Price successfully', 'success': True}, status=status.HTTP_201_CREATED)
       



class Delete_PackageBookingAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Package_Books.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Booking Deleted successfully',  'success':True}, status=status.HTTP_200_OK)



class BookingStatusWithOneAPIView(GenericAPIView):

    def get(self, request,id):
        # user = request.data.get('user')
        carts = Package_Books.objects.filter(patient=id, booking_status=1).values()
        print(carts)
        return Response({'data':carts , 'message': 'Booking Status with One Get successfully', 'success': True}, status=status.HTTP_201_CREATED)
        # return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



class UserPackagePaymentAPIView(GenericAPIView):
    serializer_class = Package_PaymentSerializer

    def post(self, request):
        package_name=""
        patient = request.data.get('patient')
        Package_Booking = request.data.get('Package_Booking')
        package_price = request.data.get('package_price')
        payment_date = request.data.get('payment_date')
        payment_status="0"

        data = Patient.objects.filter(id=patient).values()
        for i in data:
            patientname=i['patientname']
        
        dta = Package_Books.objects.filter(id=Package_Booking).values()
        for i in dta:
            package_name=i['package_name']


        serializer = self.serializer_class(data= {'patient':patient, 'patient_name':patientname,'Package_Booking':Package_Booking,'package_name':package_name,'package_price':package_price,'payment_date':payment_date,'payment_status':payment_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Payment successfull', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



class DoctorPostTreatmentDetailsAPIView(GenericAPIView):
    serializer_class = TreatmentSerializer

    def post(self, request):
        token_booking = request.data.get('token_booking')
        doctor = request.data.get('doctor')
        disease = request.data.get('disease')
        medicine = request.data.get('medicine')
        treatment_date = request.data.get('treatment_date')
        treatment_status="0"

        data = Token_Booking.objects.filter(id=token_booking).values()
        for i in data:
            patient_id=i['patient_id']

        dta = Patient.objects.filter(id=patient_id).values()
        for i in dta:
            patientname=i['patientname']
        
        dta = Doctor.objects.filter(id=doctor).values()
        for i in dta:
            doctorname=i['doctorname']


        serializer = self.serializer_class(data= {'patientname':patientname,'token_booking':token_booking,'doctor':doctor,'doctorname':doctorname,'disease':disease,'medicine':medicine,'treatment_date':treatment_date,'treatment_status':treatment_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Treatement Details Added Successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



class GetDoctorTreatmentAPIView(GenericAPIView):
    def get(self, request, id):
        doctor=""
        queryset = Doctor.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            doctor = i['id']
            print('///////////',doctor)
        instance = Treatments.objects.all().filter(doctor=doctor).values()
        print("======",instance)
        # serializer = DoctorTokenBookingSerializer(instance)
        return Response({'data': instance, 'message':'Doctor Get Treatment Details', 'success':True}, status=status.HTTP_200_OK)



class GetPatientTreatmentAPIView(GenericAPIView):
    def get(self, request, id):
        patient=""
        queryset = Token_Booking.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            t_id = i['id']
            print('///////////',t_id)
        instance = Treatments.objects.all().filter(token_booking=t_id).values()
        print("======",instance)
        # serializer = DoctorTokenBookingSerializer(instance)
        return Response({'data': instance, 'message':'Patient Get Treatment Details', 'success':True}, status=status.HTTP_200_OK)




class CartMedicineAPIView(GenericAPIView):
    serializer_class = CartSerializer

    def post(self, request):
        total_price=""
        image=""
        category=""
        p_status=""
        prices=""

        
        patient = request.data.get('patient')
        medicine=request.data.get('medicine')
        print(medicine)
        medicine_qnty = request.data.get('medicine_qnty')
        quantity=int(medicine_qnty)
        cart_status="0"
        
        carts = Cart.objects.filter(patient=patient, medicine=medicine)
        if carts.exists():
            return Response({'message':'Item is already in cart','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=Medicine.objects.all().filter(id=medicine).values()
            for i in data:
                print(i)
                prices=i['medicine_price']
                p_status=i['medicine_status']
                p_name=i['medicine_name']
                
                price=int(prices)
                print(price)
                total_price=price*quantity
                print(total_price)
                tp=str(total_price)

            producto = Medicine.objects.get(id=medicine)
            product_image = producto.medicine_photo
            
                

            serializer = self.serializer_class(data= {'patient':patient,'medicine':medicine,'medicine_qnty':medicine_qnty,'medicine_price':tp,'cart_status':cart_status,'medicine_photo':product_image,'medicine_name':p_name})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'cart added successfully', 'success':True}, status = status.HTTP_201_CREATED)
            return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)



class SingleCartAPIView(GenericAPIView):
    
    def get(self, request, id):
    
        u_id=""
        qset = Patient.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']

        data = Cart.objects.filter(patient=u_id).values()
        serialized_data = list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] = settings.MEDIA_URL + str(obj['medicine_photo'])
        return Response({'data':serialized_data, 'message':'single cart data', 'success':True}, status=status.HTTP_200_OK)





class CartIncrementQuantityAPIView(GenericAPIView):
    
    def put(self, request, id):
        cart_item = Cart.objects.get(pk=id)

        qnty=cart_item.medicine_qnty 
        qty=int(qnty)

        cart_item.medicine_qnty=qty + 1

        q=cart_item.medicine_qnty
        qn=int(q)

        pr=cart_item.medicine.medicine_price
        price=int(pr)

        tp=price*qn
        cart_item.medicine_price=tp
        
        cart_item.save()

        serialized_data = CartSerializer(cart_item, context={'request': request}).data
        base_url = request.build_absolute_uri('/')[:-1]  # Get the base URL dynamically
        serialized_data['medicine_photo'] = str(serialized_data['medicine_photo']).replace(base_url, '')

        # serialized_data['medicine_photo'] = str(serialized_data['medicine_photo']).split('http://localhost:8000')[1]
        # for obj in serialized_data:
        #     obj['image'] = settings.MEDIA_URL + str(obj['image'])
        return Response({'data': serialized_data, 'message': 'Cart item quantity updated', 'success': True}, status=status.HTTP_200_OK)


class CartDecrementQuantityAPIView(GenericAPIView):
    
    def put(self, request, id):
        cart_item = Cart.objects.get(pk=id)
        qny=cart_item.medicine_qnty
        qant=int(qny)
        if qant > 1:
            qnty=cart_item.medicine_qnty 
            qty=int(qnty)

            cart_item.medicine_qnty=qty - 1

            q=cart_item.medicine_qnty
            qn=int(q)

            pr=cart_item.medicine.medicine_price
            price=int(pr)

            tp=price*qn
            cart_item.medicine_price=tp

            cart_item.save()

            serialized_data = CartSerializer(cart_item, context={'request': request}).data
            base_url = request.build_absolute_uri('/')[:-1]  # Get the base URL dynamically
            serialized_data['medicine_photo'] = str(serialized_data['medicine_photo']).replace(base_url, '')

            # for obj in serialized_data:
            #     obj['image'] = settings.MEDIA_URL + str(obj['image'])
            return Response({'data': serialized_data, 'message': 'Cart item quantity updated', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Quantity can not be less than 1', 'success': False}, status=status.HTTP_400_BAD_REQUEST)



class Delete_CartAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Cart.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Cart Deleted successfully',  'success':True}, status=status.HTTP_200_OK)


class UserOrderAPIView(GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        patient = request.data.get('patient')
        carts = Cart.objects.filter(patient=patient, cart_status=0)

        if not carts.exists():
            return Response({'message': 'No items in cart to place order', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    
        tot = carts.aggregate(total=Sum('medicine_price'))['total']
        total=str(tot)

        print("=========total   ",total)
        # for i in total:
        #     li.append(total)
        #     print(li)


        order_data = []
        
        for i in carts:
           

            order_data.append({
                'patient': patient,
                'medicine': i.medicine.id,
                'medicine_name': i.medicine_name,
                'medicine_qnty': i.medicine_qnty,
                'medicine_price':i.medicine_price,
                'medicine_photo': i.medicine_photo,
                'order_status': "0",
                'all_price': total
            })
            print("order data==========",order_data)
            i.cart_status = "1"
            i.save()

        serializer = self.serializer_class(data=order_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Order placed successfully', 'success': True}, status=status.HTTP_201_CREATED)
        return Response({'data': serializer.errors, 'message': 'Failed', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class AllPriceAPIView(GenericAPIView):
    # serializer_class = OrderPriceSerializer

    def get(self, request,id):
        # user = request.data.get('user')
        carts = Cart.objects.filter(patient=id, cart_status=1)
        print(carts)

        tot = carts.aggregate(total=Sum('medicine_price'))['total']
        Total_prices=str(tot)
        print(tot)
        
        price_status="0"

        # serializer = self.serializer_class(data= {'user':user, 'total_price':tot,'price_status':price_status})
        # print(serializer)
        # if serializer.is_valid():
        #     serializer.save()
        return Response({'data':{ 'medicine_price':Total_prices} , 'message': 'Get Order Price successfully', 'success': True}, status=status.HTTP_201_CREATED)
        # return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)






class SingleOrderAPIView(GenericAPIView):
    def get(self, request, id):
        qset = Patient.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']

        # data=order.objects.all().filter(user=u_id).values()
        # print(data)

        data = order.objects.filter(patient=u_id).values()
        serialized_data = list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['medicine_photo'] = settings.MEDIA_URL + str(obj['medicine_photo'])
        return Response({'data':data, 'message':'single order data', 'success':True}, status=status.HTTP_200_OK)





class UserOrderPaymentAPIView(GenericAPIView):
    serializer_class = PaymentSerializer

    def post(self, request):
        user = request.data.get('user')
        amount = request.data.get('amount')
        date = request.data.get('date')
        paymentstatus="1"


        serializer = self.serializer_class(data= {'user':user, 'date':date,'amount':amount,'paymentstatus':paymentstatus})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Payment successfull', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)




# class UserPackageBookAPIView(GenericAPIView):
#     serializer_class = OrderSerializer

#     def post(self, request):
#         user = request.data.get('user')
#         carts = cart.objects.filter(user=user, cart_status=0)

#         if not carts.exists():
#             return Response({'message': 'No items in cart to place order', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
#         order_data = []
        
#         for i in carts:
#             order_data.append({
#                 'user': user,
#                 'product': i.product.id,
#                 'product_name': i.p_name,
#                 'quantity': i.quantity,
#                 'total_price': i.total_price,
#                 'image': i.image,
#                 'category': i.category,
#                 'order_status': "0",
#             })
#             print(order_data)
#             i.cart_status = "1"
#             i.save()

#         serializer = self.serializer_class(data=order_data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data, 'message': 'Order placed successfully', 'success': True}, status=status.HTTP_201_CREATED)
#         return Response({'data': serializer.errors, 'message': 'Failed', 'success': False}, status=status.HTTP_400_BAD_REQUEST)




# class SingleOrderAPIView(GenericAPIView):
#     def get(self, request, id):
#         qset = brookuser.objects.all().filter(pk=id).values()
#         for i in qset:
#             u_id=i['id']

#         # data=order.objects.all().filter(user=u_id).values()
#         # print(data)

#         data = order.objects.filter(user=u_id).values()
#         serialized_data = list(data)
#         print(serialized_data)
#         for obj in serialized_data:
#             obj['image'] = settings.MEDIA_URL + str(obj['image'])
#         return Response({'data':data, 'message':'single order data', 'success':True}, status=status.HTTP_200_OK)





# class UserOrderPaymentAPIView(GenericAPIView):
#     serializer_class = PaymentSerializer

#     def post(self, request):
#         prices=""
#         user = request.data.get('user')
#         ords = request.data.get('orders')
#         print(ords)
#         date = request.data.get('date')
#         paymentstatus="0"

#         data = order.objects.all().filter(id=ords).values()
#         print(data)
#         for i in data:
#             prices=i['price']
            
        


#         serializer = self.serializer_class(data= {'user':user, 'orders':ords,'date':date,'amount':prices,'paymentstatus':paymentstatus})
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data, 'message':'Payment successfull', 'success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)





