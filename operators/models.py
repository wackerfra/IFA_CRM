from django.db import models

class Operator(models.Model):
    COUNTRY_CHOICES = [
        ('DE', 'Germany'),
        ('AT', 'Austria'),
        ('CH', 'Switzerland'),
        ('DK', 'Denmark'),
        ('SE', 'Sweden'),
        ('NO', 'Norway'),
        ('FI', 'Finland'),
        ('NL', 'Netherlands'),
        ('BE', 'Belgium'),
        ('LU', 'Luxembourg'),
        ('PL', 'Poland'),
        ('CZ', 'Czech Republic'),
        ('SK', 'Slovakia'),
        ('HU', 'Hungary'),
        ('SI', 'Slovenia'),
        ('HR', 'Croatia'),
        ('RS', 'Serbia'),
        ('BA', 'Bosnia and Herzegovina'),
        ('ME', 'Montenegro'),
        ('AL', 'Albania'),
        ('MK', 'North Macedonia'),
        ('BG', 'Bulgaria'),
        ('RO', 'Romania'),
        ('GR', 'Greece'),
        ('TR', 'Turkey'),
        ('FR', 'France'),
        ('ES', 'Spain'),
        ('IT', 'Italy'),
    ]

    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    street = models.CharField(max_length=255)
    house_no = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    special_conditions = models.TextField(blank=True, null=True)


def __str__(self):
        return self.name
