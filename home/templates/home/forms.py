from django import forms
from .models import Feedback
from .models import contact


class FeedbackForm(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows':4,
                'placeholder': 'Enter your feedback here...',
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'
            })
        }

class ContactForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows":4, "placeholder": "your message..."}),
        required=True
    )
    class Meta:
        model = Contact
        fields = ['name', 'email']