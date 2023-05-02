from django.urls import path
from ayurveda import views

urlpatterns = [
   
   path('login_users', views.LoginUsersAPIView.as_view(), name='login_users'),

   # patient

   path('patient_register', views.PatientRegisterAPIView.as_view(), name='patient_register'),
   path('get_allpatient', views.Get_PatientAPIView.as_view(), name='get_allpatient'),
   path('single_patient/<int:id>', views.SinglePatientAPIView.as_view(), name='single_patient'),
   path('update_patient/<int:id>', views.Update_PatientAPIView.as_view(), name='update_patient'),
   path('delete_patient/<int:id>', views.Delete_PatientAPIView.as_view(), name='delete_patient'),
   path('booking_doctor', views.PatientBookDoctorAPIView.as_view(), name='booking_doctor'),
   path('get_remedy', views.Get_RemedyAPIView.as_view(), name='get_Remedy'),
   path('single_remedy/<int:id>', views.SingleRemedyAPIView.as_view(), name='single_Remedy'),
   path('get_package', views.Get_PackageAPIView.as_view(), name='get_Package'),
   path('single_package/<int:id>', views.SinglePackageAPIView.as_view(), name='single_package'),
   path('get_medicine', views.Get_MedicineAPIView.as_view(), name='get_Medicine'),
   path('single_medicine/<int:id>', views.SingleMedicineAPIView.as_view(), name='single_medicine'),
   path('patientsearch_doctor', views.PatientSearchDoctorAPIView.as_view(), name='patientsearch_doctor'),
   path('patientadd_review', views.PatientReviewAPIView.as_view(), name='patientadd_review'),
   path('patient_all_review', views.Get_ReviewAPIView.as_view(), name='patient_all_review'),
   path('single_review/<int:id>', views.SingleReviewAPIView.as_view(), name='single_review'),
   # path('patientadd_complaints', views.PatientComplaintsAPIView.as_view(), name='patientadd_complaints'),
   # path('complaint_replay/<int:id>', views.ComplaintReplayPIView.as_view(), name='complaint_replay'),
   path('patient_complaints', views.PatientComplaintsAndReplayAPIView.as_view(), name='patient_complaints'),
   path('complaintsingle_view/<int:id>', views.ComplaintAndReplayPIView.as_view(), name='complaintsingle_view'),

   path('token_booking', views.PatientBookDoctorTokenAPIView.as_view(), name='token_booking'),

   path('doctor_token_booking/<int:id>', views.DoctorTokenAPIView.as_view(), name='docor_token_booking'),

   path('patient_token_booking/<int:id>', views.PatientTokenAPIView.as_view(), name='patient_token_booking'),



   # get image
   #  path('package_image/<int:pk>', views.Get_ImageAPIView.as_view(), name='package_image'),


   # doctor

   path('doctor_register', views.DoctorRegisterAPIView.as_view(), name='doctor_register'),
   path('get_alldoctor', views.Get_DoctorAPIView.as_view(), name='get_alldoctor'),
   path('single_doctor/<int:id>', views.SingleDoctorAPIView.as_view(), name='single_doctor'),
   path('update_doctor/<int:id>', views.Update_DoctorAPIView.as_view(), name='update_doctor'),
   path('delete_doctor/<int:id>', views.Delete_DoctorAPIView.as_view(), name='delete_doctor'),
   path('doctor_view_booking/<int:id>', views.ViewDoctorBookingAPIView.as_view(), name='doctor_view_booking'),

   
   # admin

   path('admin_approve_patient/<int:id>', views.AdminApprove_PatientAPIView.as_view(), name='admin_approve_patient'),
   path('admin_approve_doctor/<int:id>', views.AdminApprove_DoctorAPIView.as_view(), name='admin_approve_doctor'),
   path('get_alldoctorbooking', views.Get_DoctorBookingAPIView.as_view(), name='get_alldoctorbooking'),

   
]



