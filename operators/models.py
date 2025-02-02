from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)  # Hotel name
    location = models.CharField(max_length=255)  # Hotel location (e.g., city)
    description = models.TextField(blank=True, null=True)  # Optional field for details
    capacity = models.IntegerField()  # Capacity of the hotel

    def __str__(self):
        return self.name

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

    SEGMENT_CHOICES = [
        (11, 'Kat. und feste Grp.'),
        (12, 'Nur feste Grp., mit ZV'),
        (13, 'Nur Amtg., Linie, Schü.'),
        (14, 'Achtung: Paketer'),
        (2, 'Vbd., Gem., Kirche'),
        (3, 'Prvt., Club, Verein'),
        (41, 'GW, KK, Partei'),
        (42, 'Firma, Business'),
        (51, 'Bus-Fili., RB, Agentur'),
        (52, 'Indi-Veranstalter'),
        (6, 'Zeitung, Medien'),
        (7, 'IFA-Gruppe'),
        (8, 'Wettbewerb'),
        (9, 'D: check. Ausl: gecheckt'),
        (10, 'VA, keine weitere Info'),
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
    internet = models.URLField(blank=True, null=True)
    segment = models.IntegerField(choices=SEGMENT_CHOICES, default=7)
    special_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    # Custom method to return the human-readable value for segments
    def get_segment_label(self):
        segment_dict = dict(self.SEGMENT_CHOICES)  # Convert choices to a dictionary
        return segment_dict.get(int(self.segment), 'Unknown')  # Retrieve label or a default



class OperatorInterest(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)  # Link to Operator
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  # Link to Hotel
    priority = models.IntegerField(default=1)  # Priority level: 1=High, 2=Medium, 3=Low
    agreement_date = models.DateField(blank=True, null=True)  # Agreement date (optional)

    class Meta:
        unique_together = (
        'operator', 'hotel')  # Prevent an operator from being linked to the same hotel multiple times

    def __str__(self):
        return f"{self.operator} - {self.hotel} (Priority {self.priority})"