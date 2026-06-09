from django import forms
from .models import Participant

class ParticipantChoiceForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Enter your username"}),
        label="Username",
    )

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        participant = Participant.objects.filter(name__iexact=username).first()
        if not participant:
            raise forms.ValidationError("Username not found. Please enter a registered participant name.")
        return participant
