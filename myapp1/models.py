from django.db import models

# Create your models here.
class Patient(models.Model):
    patientid = models.CharField(max_length=20,primary_key=True)
    patientname = models.CharField(max_length=20)
    patientpassword = models.CharField(max_length=20)
    patientphone = models.IntegerField()
   # created = models.DataTimeField(auto_now_add=True)
   # modified = models.DataTimeField(auto_now_add=True)
    def __str__(self):
        return self.patientid

    class meta:
        verbose_name_plurel = "Patient"
        db_table = 'patients'