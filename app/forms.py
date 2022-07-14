from django.forms import ModelForm, TextInput
from app.models import post

class postForm(ModelForm):
    class Meta:
        model = post
        fields = ["text"]
        widgets = {
            "text": TextInput(attrs=({"class": "form-control", "placeholder": "Write Post Here"})),
        }
