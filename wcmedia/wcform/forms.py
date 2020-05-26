from django import forms
from .models import UserInfo



class UserInfoForm(forms.ModelForm):
    
    
    class Meta:
        model = UserInfo
        fields = ['name', 'focus', 'market', 'requirement', 'domain', 'sales', 'expectation', 'audience', 'audi_you', 'market_status', 'hashtag', 'advt', 'company_profile',  'creation', 'expectation']
        