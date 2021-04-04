from django.forms import ModelForm
from .models import Create_card


class Createform(ModelForm):
    class Meta:
        model = Create_card
        fields = '__all__'
        exclude = ['user', 'random_str']
