from django import forms
from .models import CPMS, Examinees, OJTInput


class CPMSForm(forms.ModelForm):
    class Meta:
        model = CPMS
        fields = '__all__'


class ExamineesForm(forms.ModelForm):
    class Meta:
        model = Examinees
        fields = '__all__'


class OJTInputForm(forms.ModelForm):
    class Meta:
        model = OJTInput
        fields = '__all__'