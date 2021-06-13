from django import forms
from myapp.models import poll

class PollForm(forms.ModelForm):
    class Meta:
        model = poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
        widgets = {
            'question': forms.TextInput(attrs={'class':'form-control','cols': 80, 'rows': 20}),
            'option_one': forms.TextInput(attrs={'class':'form-control'}),
            'option_two': forms.TextInput(attrs={'class':'form-control'}),
            'option_three': forms.TextInput(attrs={'class':'form-control'}),
        }