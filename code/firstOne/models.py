from django.db import models


# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True)
    height = models.CharField(max_length=255, null=True)
    average_earning = models.CharField(max_length=255, null=True)
    clothes_expenses = models.CharField(max_length=255, null=True)
    makeup_expenses = models.CharField(max_length=255, null=True)
    creams_expenses = models.CharField(max_length=255, null=True)
    note = models.CharField(max_length=255, null=True)




    class Meta:
        db_table="firstone_person"

