from django.forms import ModelForm
from information.models import Scaffold

class CreateScaffoldForm(ModelForm):
    """Create a scaffold with certain fields needed"""
    class Meta:
        model = Scaffold
        fields = ['scaffold_number',
                  'scaffold_location',
                  'scaffold_for',
                  'unit'
                  ]