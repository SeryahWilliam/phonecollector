from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SERVICES = (
    ('S', 'Screen Replacement'),
    ('B', 'Battery Replacement'),
    ('W', 'Water Damage Repair'),
    ('H', 'Hardware Diagnostics'),
    ('SW', 'Software Update')
)

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.manufacturer} {self.model}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={'phone_id': self.id})

    def repaired_for_today(self):
        return self.repair_set.filter(date=date.today()).count() >= len(SERVICES)

class Repair(models.Model):
    date = models.DateField('repair date')
    service = models.CharField(
        max_length=2,
        choices=SERVICES,
        default=SERVICES[0][0]
    )
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for phone_id: {self.phone_id} @{self.url}"