from django import forms
from .models import Account,UserProfile


class RegistrationForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' Enter Password',
        'class':'form-control',
    }))
    confirm_password= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' Confirm Your Password'
    }))
    class Meta:
        model=Account
        fields=["first_name","last_name","phone_number","email","password"]
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields["first_name"].widget.attrs['placeholder']=" Enter Your Name"
        self.fields["last_name"].widget.attrs['placeholder']=" Enter Your Lastname"
        self.fields["phone_number"].widget.attrs['placeholder']=" Enter Your Name"
        self.fields["email"].widget.attrs['placeholder']=" Enter Your Email"
       
        for field in self.fields:
            self.fields[field].widget.attrs['class']="form-control"
    def clean(self):
        clean_data= super(RegistrationForm,self).clean()
        password= clean_data.get("password")
        confirm_password= clean_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does ot match! Please check again."
            )
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'    