from django import forms

from .models import Application, Course

# COURSES = (
#     ('курс №1', 'Курс №1'),
#     ('курс №2', 'Курс №2'),
#     ('курс №3', 'Курс №3')
# )

# COURSES = Course.objects.filter(name=Course.name)

class AppicationForm(forms.ModelForm):

    class Meta:
        model = Application
        # course = forms.ChoiceField(choices=COURSES)
        fields = ('name', 'email', 'phone', 'course', 'comment')


class RawApplicationForm(forms.Form):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Ім'я"}))
    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': "Email"}))
    phone = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Номер телефону"}))
    course = forms.ModelChoiceField(queryset=Course.objects.all().order_by('title'))
    # course = forms.CharField(required=True, label="", widget=forms.Select(choices=COURSES))
    comment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'placeholder': "Коментар"}))