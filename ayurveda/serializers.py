from rest_framework import serializers
from .models import Log, Patient, Doctor, Doctor_Booking, Remedy, Packages, Medicine, Review

class LoginUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class PatientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    def create(self, validated_data):
        return Patient.objects.create(**validated_data)



class doctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__' 
    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)


class DoctorBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Booking
        fields = '__all__' 
    def create(self, validated_data):
        return Doctor_Booking.objects.create(**validated_data)



class RemedySerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedy
        fields = '__all__' 


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__' 


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__' 



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__' 
    def create(self, validated_data):
        return Review.objects.create(**validated_data)
    
