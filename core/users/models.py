from django.db import models

class User(models.Model):
    first_name = models.CharField("El nombre de la persona", max_length=100)
    last_name = models.CharField("El apellido de la persona", max_length=100)
    cars = models.ManyToManyField('Car', verbose_name="Los carros del usuario")
    
STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Acepted'),
)

class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)