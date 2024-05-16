from django.db import models

# Create your models here.
class Gender(model.Model):
    gender_id = models.BigAutoField(primary_key=True)
    gender = models.charField(maxlength=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=Tue)

class Meta:
    db_table = 'genders'
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max|length=55)
    middle_name = models.CharField(max_length=55, balck=True)
    last_name = models.CharField(max_legnth=55)
    age = models.IntegrField()
    birth_date = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55)
    password = models.CharField(max_lenght=55)