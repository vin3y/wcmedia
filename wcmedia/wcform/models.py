from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length = 100, help_text= 'Enter Your Company Name',  verbose_name= 'Company Name')
    focus = models.CharField(max_length = 200, help_text= 'Enter Your Company Focus',  verbose_name= 'Company Focus')
    market = models.CharField(max_length = 200, help_text= 'Enter Your Company Market Field',  verbose_name= 'Things You Market')
    requirement = models.CharField(max_length = 300, help_text='Write Down Your Company Requirements',  verbose_name= 'Company Requirement')
    domain = models.CharField(max_length = 200, help_text='Enter Your Domain', verbose_name= 'Comapny Domain')
    sales = models.CharField(max_length = 400, help_text= 'Your Sales Stratergy', verbose_name= 'Sales Stratergy')
    expectation = models.CharField(max_length = 400, help_text= 'What Do You Expect From Us?' ,verbose_name= 'Company Expectation')
    audience = models.CharField(max_length = 400, help_text= 'Type of audience they want to build', verbose_name= 'Audeince You Want')
    audi_you = models.CharField(max_length= 400, help_text= 'Type Of Audeince You Currently Own', verbose_name= 'Audience You Have')
    market_status = models.CharField(max_length = 400, help_text= 'Previous Market Status', verbose_name= 'Market Status')
    hashtag = models.CharField(max_length = 100, help_text= 'Specific Hashtag', verbose_name= 'Hashtags Used')
    advt = models.CharField(max_length = 400, help_text= 'Preveious Advertisement Stratergy', verbose_name= 'Advertisement Startergy')
    company_profile = models.URLField(blank= False, help_text= 'Company Profile Link', verbose_name= 'Company Profile')
    creation = models.CharField(max_length = 400, help_text= 'Content creation( Should we build our own / Creative design )', verbose_name= ' Content Creation')
    expected = models.CharField(max_length = 7,blank= False, help_text= 'Expected Price', verbose_name= 'Price', null= False)
    
    class Meta:
        ordering = ['-name',]
        
    def __str__(self):
        return self.name
    
    