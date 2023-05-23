from django import forms
from .models import PersonToContact
import bleach

class PersonToContactForm(forms.ModelForm):
    class Meta:
        model = PersonToContact
        fields = ['name', 'surname', 'email', 'topic', 'text', 'phone_number']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = bleach.clean(instance.name)
        instance.surname = bleach.clean(instance.surname)
        instance.email = bleach.clean(instance.email)
        instance.topic = bleach.clean(instance.topic)
        instance.text = bleach.clean(instance.text)
        instance.phone_number = bleach.clean(instance.phone_number)

        if commit:
            instance.save()
        return instance

