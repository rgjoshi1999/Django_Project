from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback, ContactUs#, Payment
from django import forms

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class Feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields = ['username','feedback']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'mobile_number','Course']

'''
class PaymentForm(forms.Form):
    class Meta:
        model = Payment
        fields = ['amount','card_number','exp_month','exp_year','cvc']
'''