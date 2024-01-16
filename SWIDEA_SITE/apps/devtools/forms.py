from django import forms
from .models import *

class DevtoolForm(forms.ModelForm):
    class Meta():
        model = Devtool
        fields = ('__all__')