from django import forms
from .models import Board

class BoardUpdateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject', 'content', 'create_date']
