from django import forms
from django.contrib.auth.models import User
from chess.models import savedGameChess


class savedGameFormChess(forms.ModelForm):
    match = forms.CharField(widget= forms.TextInput
                           (attrs={'id':'match',}))
    class Meta():
        model = savedGameChess
        fields = ('match', )
