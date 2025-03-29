from django import forms
from payment.models import ShippingAddress

class Shippingform(forms.ModelForm):
    shippingfull_name=forms.CharField(label="Full Name:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Full Name', 'class': 'form-control'}),required=True)
    shipping_EmailAddress=forms.CharField(label="Email Address:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email Address', 'class': 'form-control'}),required=True)
    shipping_phonenumber=forms.CharField(label="Phone Number:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number', 'class': 'form-control'}),required=True)
    shipping_country=forms.CharField(label="Country:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Country', 'class': 'form-control'}),required=True)
    shipping_state=forms.CharField(label="State:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State', 'class': 'form-control'}),required=True)
    shipping_district=forms.CharField(label="District:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'District', 'class': 'form-control'}),required=True)
    
    shipping_city=forms.CharField(label="City:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'city', 'class': 'form-control'}),required=True)
    shipping_zipCode=forms.CharField(label="Zip Code:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zip Code', 'class': 'form-control'}),required=True)
    class Meta:
        model = ShippingAddress
        fields = ['shippingfull_name', 'shipping_EmailAddress', 'shipping_phonenumber', 'shipping_country', 'shipping_state', 'shipping_district', 'shipping_city', 'shipping_zipCode']
        exclude = ['user']
        
        
class PaymentForm(forms.Form):
    card_name=forms.CharField(label="Card Name:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Name on Card', 'class': 'form-control'}))
    card_number=forms.CharField(label="Card Number:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Card Number', 'class': 'form-control'}),required=True)
    card_exp_date=forms.CharField(label="Expiry Date:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'MM/YY', 'class': 'form-control'}),required=True)
    card_cvv=forms.CharField(label="CVV:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'CVV', 'class': 'form-control'}),required=True)
    card_zip=forms.CharField(label="Zip Code:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zip Code', 'class': 'form-control'}),required=True)
    card_address=forms.CharField(label="Address:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Payment Address', 'class': 'form-control'}),required=True)
    card_city=forms.CharField(label="City:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City', 'class': 'form-control'}),required=True)
    card_state=forms.CharField(label="State:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State', 'class': 'form-control'}),required=True)
    card_country=forms.CharField(label="Country:",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Country', 'class': 'form-control'}),required=True)

    
            