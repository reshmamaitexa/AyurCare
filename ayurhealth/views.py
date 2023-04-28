from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ayurveda.models import Patient, Log, Doctor, Remedy, Packages, Medicine
from ayurveda import models


# Create your views here.

def index(request):
    return render(request,"index.html")


def admin_login(request):
    return render(request,"managers/user-login.html")


def admin_dashboard(request):
    return render(request, 'managers/index.html')

# --------------------------------- admin login ------------------------------

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request, 'managers/index.html')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('admin_login')

    else:
        return render(request, 'user_login.html')

# -------------------------------------- admin view all patients --------------------------

def admin_view_allpatients(request):
    queryset = Patient.objects.all()
    return render(request,'managers/pending-patients.html',{'queryset':queryset})


# -------------------------------------- admin view all approved patients --------------------------

def admin_view_all_approved_patients(request):
    queryset = Patient.objects.all()
    return render(request,'managers/approved-patients.html',{'queryset':queryset})


# -------------------------------------- admin view approve patients --------------------------

def admin_approve_patients(request,id):
    user = Patient.objects.get(id=id)
    user.patientstatus = 1
    user.save()
    return redirect('admin_view_all_approved_patients')


# -------------------------------------- admin view reject patients --------------------------

def admin_reject_patients(request,id):
    delmember = Patient.objects.get(id=id)
    print(delmember)
    print(delmember.log_id)
    l_id=delmember.log_id
    print(l_id)
    data=Log.objects.get(username=l_id)
    data.delete()
    return redirect('admin_view_allpatients')


# -------------------------------------- admin add/view/edit/delete doctors --------------------------

def admin_add_doctorpage(request):
    return render(request,"managers/add_doctor.html")


def admin_add_doctor(request):
    if request.method == 'POST':
        login_id=''
        doctorname = request.POST.get('doctorname')
        doctorqualification = request.POST.get('doctorqualification')
        doctorexperience = request.POST.get('doctorexperience')
        doctoremail = request.POST.get('doctoremail')
        doctorphone = request.POST.get('doctorphone')
        doctorspecialization = request.POST.get('doctorspecialization')
        doctorgender = request.POST.get('doctorgender')
        doctor_available_days = request.POST.get('doctor_available_days')
        doctor_available_time = request.POST.get('doctor_available_time')
        doctorprofile_photo = request.FILES['doctorprofile_photo']
        doctorusername = request.POST.get('doctorusername')
        doctorpassword = request.POST.get('doctorpassword')
        role = 'doctor'
        doctorstatus = '1'


        if (Log.objects.filter(username=doctorusername)):
            return redirect('admin_add_doctorpage')

        else:
            user_login = models.Log(username= doctorusername, password=doctorpassword, role=role)
            user_login.save()

            UserDetails = models.Doctor(doctorname=doctorname, doctorqualification=doctorqualification,doctorexperience=doctorexperience, doctoremail=doctoremail, doctorphone=doctorphone, doctorspecialization=doctorspecialization, doctorgender=doctorgender, doctor_available_days=doctor_available_days, doctor_available_time=doctor_available_time, doctorprofile_photo=doctorprofile_photo,log_id=user_login, doctorstatus=doctorstatus,role=role)
            UserDetails.save()
            
        return redirect('admin_view_doctors')
    else:
        return render(request, 'managers/add_doctor.html')


def admin_view_doctors(request):
    data=Doctor.objects.all()
    return render(request,"managers/all_doctors.html",{'data':data})



def admineditdoctor(request,id):
        Data = Doctor.objects.get(id=id)
        return render(request,'managers/admineditdoctor.html',{'Data':Data})


def doctorformupdate(request,id):
        if request.method=="POST":
            add=Doctor.objects.get(id=id)
            add.doctorname=request.POST["doctorname"]
            add.doctorqualification=request.POST["doctorqualification"]
            add.doctorexperience=request.POST["doctorexperience"]
            add.doctoremail=request.POST['doctoremail']
            add.doctorphone=request.POST["doctorphone"]
            add.doctorspecialization=request.POST["doctorspecialization"]
            add.doctorgender=request.POST['doctorgender']
            add.doctor_available_days=request.POST["doctor_available_days"]
            add.doctor_available_time=request.POST['doctor_available_time']
            add.save()
            return redirect("admin_view_doctors")


def admin_reject_doctors(request,id):
    delmember = Doctor.objects.get(id=id)
    print(delmember)
    print(delmember.log_id)
    l_id=delmember.log_id
    print(l_id)
    data=Log.objects.get(username=l_id)
    data.delete()
    return redirect('admin_view_doctors')


#  ----------------------------------------- admin add/view/edit/delete remedy -----------------------------------------------

def admin_add_remedy(request):
    return render(request,"managers/add_remedies.html")


def admin_add_allremedy(request):
    if request.method == 'POST':
        disease = request.POST.get('disease')
        symptoms = request.POST.get('symptoms')
        remedy = request.POST.get('remedy')
        remedy_photo = request.FILES['remedy_photo']
        remedystatus = '0'
        RemedyDetails = models.Remedy(disease=disease, symptoms=symptoms,remedy=remedy, remedy_photo=remedy_photo,remedystatus=remedystatus)
        RemedyDetails.save()
            
        return redirect('admin_view_remedy')
    else:
        return render(request, 'managers/add_remedies.html')



def admin_view_remedy(request):
    data=Remedy.objects.all()
    print(data)
    return render(request,"managers/view_remedies.html",{'data':data})



def admin_delete_remedy(request,id):
    delmember = Remedy.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_view_remedy')


def admin_edit_remedy(request,id):
    Data = Remedy.objects.get(id=id)
    return render(request,'managers/admin_edit_remedy.html',{'Data':Data})


def remedyformupdate(request,id):
    if request.method=="POST":
        add=Remedy.objects.get(id=id)
        add.disease=request.POST["disease"]
        add.symptoms=request.POST["symptoms"]
        add.remedy=request.POST["remedy"]
        add.save()
        return redirect("admin_view_remedy")



#  ----------------------------------------- admin add/view/edit/delete remedy -----------------------------------------------

def admin_add_package_page(request):
    return render(request,"managers/admin_add_package.html")


def admin_add_packages(request):
    if request.method == 'POST':
        package_name = request.POST.get('package_name')
        package_goal = request.POST.get('package_goal')
        package_description = request.POST.get('package_description')
        package_duration = request.POST.get('package_duration')
        package_price = request.POST.get('package_price')
        package_photo = request.FILES['package_photo']
        package_status = '0'
        PackageDetails = models.Packages(package_name=package_name, package_goal=package_goal,package_description=package_description, package_duration=package_duration,package_price=package_price,package_photo=package_photo,package_status=package_status)
        PackageDetails.save()
            
        return redirect('admin_view_packages')
    else:
        return render(request, 'managers/admin_add_package.html')



def admin_view_packages(request):
    data=Packages.objects.all()
    print(data)
    return render(request,"managers/admin_view_packages.html",{'data':data})



def admin_delete_package(request,id):
    delmember = Packages.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_view_packages')


def admin_edit_packages(request,id):
    Data = Packages.objects.get(id=id)
    return render(request,'managers/admin_edit_packages.html',{'Data':Data})


def packageformupdate(request,id):
    if request.method=="POST":
        add=Packages.objects.get(id=id)
        add.package_name=request.POST["package_name"]
        add.package_goal=request.POST["package_goal"]
        add.package_description=request.POST["package_description"]
        add.package_duration=request.POST["package_duration"]
        add.package_price=request.POST["package_price"]
        add.save()
        return redirect("admin_view_packages")



#  ----------------------------------------- admin add/view/edit/delete medicine -----------------------------------------------

def admin_add_medicine_page(request):
    return render(request,"managers/admin_add_medicine.html")


def admin_add_medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        medicine_qnty = request.POST.get('medicine_qnty')
        medicine_description = request.POST.get('medicine_description')
        medicine_dosage = request.POST.get('medicine_dosage')
        medicine_usage = request.POST.get('medicine_usage')
        medicine_price = request.POST.get('medicine_price')
        medicine_photo = request.FILES['medicine_photo']
        medicine_status = '0'
        MedicineDetails = models.Medicine(medicine_name=medicine_name, medicine_qnty=medicine_qnty,medicine_description=medicine_description, medicine_dosage=medicine_dosage,medicine_usage=medicine_usage,medicine_price=medicine_price,medicine_photo=medicine_photo,medicine_status=medicine_status)
        MedicineDetails.save()
            
        return redirect('admin_view_medicine')
    else:
        return render(request, 'managers/admin_add_medicine.html')



def admin_view_medicine(request):
    data=Medicine.objects.all()
    print(data)
    return render(request,"managers/admin_view_medicine.html",{'data':data})



def admin_delete_medicine(request,id):
    delmember = Medicine.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_view_medicine')


def admin_edit_medicine(request,id):
    Data = Medicine.objects.get(id=id)
    return render(request,'managers/admin_edit_medicine.html',{'Data':Data})


def medicineformupdate(request,id):
    if request.method=="POST":
        add=Medicine.objects.get(id=id)
        add.medicine_name=request.POST["medicine_name"]
        add.medicine_qnty=request.POST["medicine_qnty"]
        add.medicine_description=request.POST["medicine_description"]
        add.medicine_dosage=request.POST["medicine_dosage"]
        add.medicine_usage=request.POST["medicine_usage"]
        add.medicine_price=request.POST["medicine_price"]
        add.save()
        return redirect("admin_view_medicine")
    