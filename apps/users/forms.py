from django import forms
from django.contrib.auth.models import User
from .models import ExtendedGroup


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "group"]

    username = forms.CharField(label="User Nickname", max_length=150)
    group = forms.ModelChoiceField(
        queryset=ExtendedGroup.objects.all(), required=True, label="Group"
    )

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
            user.groups.clear()
            user.groups.add(self.cleaned_data["group"])
        return user


class ExtendedGroupForm(forms.ModelForm):
    class Meta:
        model = ExtendedGroup
        fields = ["name", "description"]

    name = forms.CharField(
        label="Name",
        max_length=80,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text="Required. 80 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        required=False,
    )
