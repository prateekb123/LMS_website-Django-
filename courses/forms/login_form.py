from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login
from django.forms import ValidationError

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length= 25, required = True, label='Email Address')

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email = email)
            result = authenticate(username = user.username, password = password)
            print("result", result)

            if result == None:
                raise ValidationError("Email and Password Incorrect")
                
            else:
                login(self.request, result)
                return result
                


        except:
            raise ValidationError("Email or Password Incorrect")



     

    