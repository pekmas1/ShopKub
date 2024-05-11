from django import forms
from .models import UserProfile

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'tel_number', 'profile_picture']
        widgets = {
            "address": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
            "tel_number": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
            "profile_picture": forms.FileInput(attrs={
                "class": INPUT_CLASSES
            }),
        }