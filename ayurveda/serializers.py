from rest_framework import serializers
from .models import Log, Patient, Doctor, Doctor_Booking, Remedy, Packages, Medicine, Review, Complaints, Complaints_Replay, ComplaintsAndReplay, Token_Booking, Package_Booking, Package_payment, Medicine_Carts, Medicine_orders

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


class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__' 
    def create(self, validated_data):
        return Complaints.objects.create(**validated_data)


class ComplaintReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints_Replay
        fields = '__all__' 


class ComplaintsAndReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintsAndReplay
        fields = '__all__' 
    def create(self, validated_data):
        return ComplaintsAndReplay.objects.create(**validated_data)


class DoctorTokenBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token_Booking
        fields = '__all__' 
    def create(self, validated_data):
        return Token_Booking.objects.create(**validated_data)


class PackageBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package_Booking
        fields = '__all__'
    def create(self,validated_data):
        return Package_Booking.objects.create(**validated_data)


class Package_PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package_payment
        fields = '__all__'
    def create(self,validated_data):
        return Package_payment.objects.create(**validated_data)


class MedicineCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine_Carts
        fields = '__all__'
    def create(self,validated_data):
        return Package_Cart.objects.create(**validated_data)


class Medicine_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine_orders
        fields = '__all__'
    def create(self,validated_data):
        return Package_order.objects.create(**validated_data)
    
