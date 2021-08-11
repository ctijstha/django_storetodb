

from django.forms import ModelForm
from cal.models import Information


class InformationForm(ModelForm):
    
    class Meta:
        model = Information
        fields =["name","email","address","contact"]

    