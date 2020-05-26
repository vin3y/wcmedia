from django import forms
from .models import UserInfo



class UserInfoForm(forms.ModelForm):
    
    
    class Meta:
        model = UserInfo
        fields = ['name', 'focus', 'market', 'requirement', 'domain', 'sales', 'expectation', 'audience', 'audi_you', 'market_status', 'hashtag', 'advt', 'company_profile',  'creation', 'expectation']
        widgets = { 'name': forms.TextInput(attrs={'size': 50})
                    , 'focus': forms.TextInput(attrs={'size': 50})
                    , 'market': forms.Textarea()
                    , 'requirement': forms.Textarea() 

                    , 'domain': forms.TextInput(attrs={'size': 100})
                    , 'sales': forms.Textarea()
                    , 'expectation': forms.Textarea() 

                    , 'audience': forms.TextInput(attrs={'size': 100})
                    , 'audi_you': forms.TextInput(attrs={'size': 100})
                    , 'market_status': forms.Textarea()
                    , 'hashtag': forms.TextInput(attrs={'size': 100})
                    , 'advt': forms.Textarea()
                    , 'company_profile': forms.TextInput(attrs={'size': 100})
                    , 'creation': forms.TextInput(attrs={'size': 100})
                    , 'expectation': forms.TextInput(attrs={'size': 20})
                 }