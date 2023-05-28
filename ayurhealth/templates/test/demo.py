
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




class MedicineCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine_Carts_tb
        fields = '__all__'
    def create(self,validated_data):
        return Medicine_Carts_tb.objects.create(**validated_data)


class Medicine_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine_order_tb
        fields = '__all__'
    def create(self,validated_data):
        return Medicine_order_tb.objects.create(**validated_data)
