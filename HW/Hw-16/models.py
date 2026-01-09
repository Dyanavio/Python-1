from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    specialization = models.CharField(_("Specialization"), max_length=50)
    address = models.CharField(_("Address"), max_length=50)
    website = models.CharField(_("Website"), max_length=50)
    phone = models.CharField(_("Phone"), max_length=50)

    def __str__(self) -> str:
        return f"{self.name}  |  {self.specialization}  |  {self.address}  |  {self.website}  |  {self.phone}"