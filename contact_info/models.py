from django.db import models

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('Family', 'Family'),
        ('Friend', 'Friend'),
        ('Business', 'Business'),
        ('Networking', 'Networking'),
        ('Other', 'Other'),
    ]

    CONNECTED_SOURCE_CHOICES = [
        ('Education', 'Education'),
        ('Job', 'Job'),
        ('Business', 'Business'),
        ('Networking', 'Networking'),
        ('Social Media', 'Social Media'),
        ('Family', 'Family'),
        ('Other', 'Other'),
    ]

    SCOPE_CHOICES = [
        ('Investor', 'Investor'),
        ('Consultant', 'Consultant'),
        ('Freelancer', 'Freelancer'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Supporter', 'Supporter'),
        ('Investor', 'Investor'),
        ('Consultant', 'Consultant'),
        ('Freelancer', 'Freelancer'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    profession = models.CharField(max_length=100)
    dob = models.DateField(verbose_name='Date of Birth')
    connected_year = models.PositiveIntegerField()
    connected_source = models.CharField(max_length=20, choices=CONNECTED_SOURCE_CHOICES)
    working_place = models.CharField(max_length=100)
    native_place = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name