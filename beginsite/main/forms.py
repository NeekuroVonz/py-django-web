from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=255, required=True)
    check = forms.BooleanField(required=False)
    
class CreateNewItem(forms.Form):
    pass