from django.db import models

BIRTH_YEAR_CHOICES = (
    ('1980', '1980'),
    ('1981', '1981'),
    ('1982', '1982'),
    ('1983', '1983'),
    ('1984', '1984'),
)

FAVORITE_COLORS_CHOICES = (
    ('az', 'Azul'),
    ('vd', 'Verde'),
    ('pt', 'Preto'),
)

class Client(models.Model):
    name=models.CharField(max_length=200)
    birth_year=models.DateField()
    birth_year1=models.CharField(max_length=4, choices=BIRTH_YEAR_CHOICES)
    favorite_colors=models.CharField(max_length=2, choices=FAVORITE_COLORS_CHOICES)

    def __str__(self):
        return self.name