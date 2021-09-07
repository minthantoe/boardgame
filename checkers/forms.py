from django import forms
from django.contrib.auth.models import User
from checkers.models import savedGameCheckers

class savedGameFormCheckers(forms.ModelForm):
    match = forms.CharField(widget= forms.TextInput
                           (attrs={'id':'match',}))
    class Meta():
        model = savedGameCheckers
        fields = ('match', )
