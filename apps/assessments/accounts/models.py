from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('REVIEWER', 'Reviewer'),
        ('REQUESTER', 'Requester'),
        ('VENDOR', 'Vendor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    org = models.ForeignKey('orgs.Organization', null=True, blank=True, on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendors.Vendor', null=True, blank=True, on_delete=models.CASCADE)
