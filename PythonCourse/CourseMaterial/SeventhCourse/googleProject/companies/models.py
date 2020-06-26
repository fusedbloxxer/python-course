from django.db import models

# Create your models here.
from location.models import Location

company_choices = (('S.R.L', 'S.R.L.'), ('S.A.', 'S.A.'))


class Companies(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=company_choices)
    active = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} from {self.location.city} city - {self.location.country}"
