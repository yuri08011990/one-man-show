from django import forms
from .models import Application, Course


class AppicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name', 'email', 'phone', 'course', 'comment')


class RawApplicationForm(forms.Form):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Ім'я", 'style': 'width: 340px'}))
    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': "Email", 'style': 'width: 340px'}))
    phone = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Номер телефону", 'style': 'width: 340px'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all().order_by('title'), label='', empty_label='Оберіть курс', widget=forms.Select(attrs={'style': 'width: 340px'}))
    comment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'placeholder': "Коментар (не обов'язково)", 'rows': 2, 'style': 'width: 340px'}))