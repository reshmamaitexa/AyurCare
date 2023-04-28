from django.urls import path
from ayurhealth import views

urlpatterns = [
   
   path('', views.index, name='index'),
   path('admin_login', views.admin_login, name='admin_login'),
   path('login_admin', views.login_admin, name='login_admin'),
   path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

   path('admin_view_allpatients', views.admin_view_allpatients, name='admin_view_allpatients'),
   path('admin_view_all_approved_patients', views.admin_view_all_approved_patients, name='admin_view_all_approved_patients'),
   path('admin_approve_patients/<int:id>', views.admin_approve_patients, name='admin_approve_patients'),
   path('admin_reject_patients/<int:id>', views.admin_reject_patients, name='admin_reject_patients'),

   path('admin_add_doctorpage', views.admin_add_doctorpage, name='admin_add_doctorpage'),
   path('admin_add_doctor', views.admin_add_doctor, name='admin_add_doctor'),
   path('admin_view_doctors', views.admin_view_doctors, name='admin_view_doctors'),
   path('admineditdoctor/<int:id>', views.admineditdoctor, name='admineditdoctor'),
   path('admin_reject_doctors/<int:id>', views.admin_reject_doctors, name='admin_reject_doctors'),
   path('<int:id>/doctorformupdate/', views.doctorformupdate, name='doctorformupdate'),

   path('admin_add_remedy', views.admin_add_remedy, name='admin_add_remedy'),
   path('admin_add_allremedy', views.admin_add_allremedy, name='admin_add_allremedy'),
   path('admin_view_remedy', views.admin_view_remedy, name='admin_view_remedy'),
   path('admin_delete_remedy/<int:id>', views.admin_delete_remedy, name='admin_delete_remedy'),
   path('admin_edit_remedy/<int:id>', views.admin_edit_remedy, name='admin_edit_remedy'),
   path('<int:id>/remedyformupdate/', views.remedyformupdate, name='remedyformupdate'),

   path('admin_add_package_page', views.admin_add_package_page, name='admin_add_package_page'),
   path('admin_add_packages', views.admin_add_packages, name='admin_add_packages'),
   path('admin_view_packages', views.admin_view_packages, name='admin_view_packages'),
   path('admin_delete_package/<int:id>', views.admin_delete_package, name='admin_delete_package'),
   path('admin_edit_packages/<int:id>', views.admin_edit_packages, name='admin_edit_packages'),
   path('<int:id>/packageformupdate/', views.packageformupdate, name='packageformupdate'),

   path('admin_add_medicine_page', views.admin_add_medicine_page, name='admin_add_medicine_page'),
   path('admin_add_medicine', views.admin_add_medicine, name='admin_add_medicine'),
   path('admin_view_medicine', views.admin_view_medicine, name='admin_view_medicine'),
   path('admin_delete_medicine/<int:id>', views.admin_delete_medicine, name='admin_delete_medicine'),
   path('admin_edit_medicine/<int:id>', views.admin_edit_medicine, name='admin_edit_medicine'),
   path('<int:id>/medicineformupdate/', views.medicineformupdate, name='medicineformupdate'),



]