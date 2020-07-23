from django import forms
from .models import Application, Course


class AppicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name', 'email', 'phone', 'course', 'comment')


class RawApplicationForm(forms.Form):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Ім'я"}))
    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': "Email"}))
    phone = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Номер телефону"}))
    course = forms.ModelChoiceField(queryset=Course.objects.all().order_by('title'))
    comment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'placeholder': "Коментар"}))