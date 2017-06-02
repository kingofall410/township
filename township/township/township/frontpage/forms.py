from django.db import models
from django.forms import ModelForm

from township.frontpage.models import Location

class WelcomeForm(ModelForm):
    class Meta:
        model = Location
        fields = ["state", "muni"]