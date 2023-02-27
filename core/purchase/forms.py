from django import forms
from .models import PurchaseModel


class PurchaseForm(forms.ModelForm):

    quant = forms.IntegerField(initial=0) 
    class Meta:
        model = PurchaseModel
        fields = ["product", "quant"]
        

       