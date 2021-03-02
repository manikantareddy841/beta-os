from django.db import models
from multiselectfield import MultiSelectField

class enquarydata(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)

    courses_choices=(
        ('python','python'),
        ('django','django'),
        ('ui','ui'),
        ('restapi','restapi')
    )
    courses=MultiSelectField(choices=courses_choices,max_length=200)

    trainers_choices=(
        ('mani','mani'),
        ('guru','guru'),
        ('chinna','chinna')
    )
    trainers=MultiSelectField(choices=trainers_choices,max_length=200)

    location_choices=(
        ('hyd','hyd'),
        ('bangalore','bangalore'),
        ('chennai','chennai'),
        ('delhi','delhi')
    )
    locations=MultiSelectField(choices=location_choices,max_length=200)

    gender=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)




# Create your models here.
