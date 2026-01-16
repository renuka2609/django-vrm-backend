from django.db import models
from apps.orgs.models import Organization

class Vendor(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
