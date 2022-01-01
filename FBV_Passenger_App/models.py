from django.db import models

# Create your models here.
class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    rewardpoint = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self) -> str:
        return self.firstname+self.lastname+self.rewardpoint