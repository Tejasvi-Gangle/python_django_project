from django import forms
from products.models import Review,Contact

class Reviewform(forms.ModelForm):
    class Meta:
        model=Review
        fields={"Name","Title","Description"}
class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"Name","Mobile","Email","General_Enquiry"}