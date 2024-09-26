from django.db import models

class Business(models.Model):
    LEVEL_CHOICES = [
        ('HO', 'Head Office'),
        ('BR', 'Branch'),
        ('SA', 'Stand Alone'),
        ('OT', 'Other')
    ]
    TYPE_CHOICES = [
        ('PROD', 'Production'),
        ('TRAD', 'Trading'),
        ('SERV', 'Service'),
        ('OT', 'Other')
    ]
    CATEGORY_CHOICES = [
        ('GCB', 'Global Corporate Brand'),
        ('CB', 'Corporate Brand'),
        ('RB', 'Regional Brand'),
        ('LBB', 'Local Big Brand'),
        ('LB', 'Local Brand'),
        ('NRI', 'NRI Brand'),
        ('OT', 'Other')
    ]
    
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    name_of_firm = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    website_url = models.URLField(max_length=200)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name_of_firm


class ContactPerson(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='contact_persons')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    native_town = models.CharField(max_length=100, blank=True, null=True)  # Add this field
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)  # Add this field
    remarks = models.TextField(blank=True, null=True)  # Add this field

    def __str__(self):
        return self.name
