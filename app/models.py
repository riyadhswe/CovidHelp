from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=50, null= False,blank=False)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50, null= False,blank=False)
    state = models.ForeignKey(Division , on_delete=models.CASCADE,related_name='cities')

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=50, null= False,blank=False)
    phone = models.CharField(max_length=50, null= False,blank=False)
    address = models.CharField(max_length=50, null= False,blank=False)
    city = models.ForeignKey(City , on_delete=models.CASCADE,related_name='hospitals')

    def __str__(self):
        return self.name

class Service(models.Model):
    hospital = models.OneToOneField(Hospital,on_delete=models.CASCADE,primary_key=True)
    oxygen_bed_total = models.IntegerField(default=0)
    oxygen_bed_available = models.IntegerField(default=0)
    oxygen_cylinder_total = models.IntegerField(default=0)
    ventilator_total = models.IntegerField(default=0)
    ventilator_available = models.IntegerField(default=0)

    def __str__(self):
        return self.hospital