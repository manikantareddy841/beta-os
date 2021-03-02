from django import forms
from multiselectfield import MultiSelectFormField



class enquaryform(forms.Form):
    name=forms.CharField(
        label='Enter Your Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Name'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Your Mobile Number:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your mobile Number'
            }
        )
    )

    email=forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your email id'
            }
        )
    )
    couses_choices=(
        ('python','python'),
        ('django','django'),
        ('ui','ui'),
        ('restapi','restapi')
    )
    courses=MultiSelectFormField(choices=couses_choices,label='Select Required courses:')

    trainers_choices=(
        ('mani','mani'),
        ('guru','guru'),
        ('chinna','chinna')
    )
    trainers=MultiSelectFormField(choices=trainers_choices,label='select Required Trainers:')

    location_choices=(
        ('hyd','hyd'),
        ('bangalore','bangalore'),
        ('chennai','chennai'),
        ('delhi','delhi')
    )

    locations=MultiSelectFormField(choices=location_choices,label='Select Required Locations')


    gender_choices=(
        ('male','male'),
        ('female','female')
    )
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect())

