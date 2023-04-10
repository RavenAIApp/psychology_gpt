from django.db import models

# Create your models here.

#Doctor, add id automatic
class Doctor(models.Model):
    Name = models.CharField(max_length=64) #CharFiled, max_length needed
    AddedTime = models.DateTimeField(auto_now_add=True) #创建的时候默认值
    LastUpdated = models.DateTimeField(auto_now=True) #最近更新时间

    class Meta:
        managed = True
        db_table = 'MIND_Doctor'

#Patient, add id automatic
class Patient(models.Model):
    GENDER_CHOICES = (
        (0, 'Undefined'),
        (1, 'Male'),
        (2, 'Female'),
	)
    DoctorID = models.ForeignKey(to="Doctor", to_field="id", on_delete=models.SET_NULL, null=True, blank=True) #CharFiled, max_length needed
    Name = models.CharField(max_length=64) #CharFiled, max_length needed
    Gender = models.SmallIntegerField(choices=GENDER_CHOICES, default = 0)
    Age = models.SmallIntegerField(null=True, blank=True)
    Address = models.CharField(max_length=256, null=True, blank=True)
    Phone= models.CharField(max_length=24, null=True, blank=True)
    Case= models.TextField(null=True, blank=True)
    AddedTime = models.DateTimeField(auto_now_add=True) #创建的时候默认值
    LastUpdated = models.DateTimeField(auto_now=True) #最近更新时间

    class Meta:
        managed = True
        db_table = 'MIND_Patient'

#Record, add id automatic
class Record(models.Model):
    PROCESS_CHOICES = (
        (0, 'Pre-doctor'),
        (1, 'Doctor'),
        (2, 'Post-doctor'),
	)
    STAGE_CHOICES = (
        (0, 'Opening'),
        (1, 'Clarification'),
        (2, 'Exploring'),
        (3, 'Wrapping'),
	)
    PatientID = models.ForeignKey(to="Patient", to_field="id", on_delete=models.CASCADE) #CharFiled, max_length needed
    Process = models.SmallIntegerField(choices=PROCESS_CHOICES, default = 0)
    Stage = models.SmallIntegerField(choices=STAGE_CHOICES, default = 0)
    Description = models.TextField(null=True, blank=True)
    Reply = models.TextField(null=True, blank=True)
    AddedTime = models.DateTimeField(auto_now_add=True) #创建的时候默认值
    LastUpdated = models.DateTimeField(auto_now=True) #最近更新时间

    class Meta:
        managed = True
        db_table = 'MIND_Record'
