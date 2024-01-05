from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musicians.models import Musician

class Album(models.Model):
    Album_Name = models.CharField(max_length=50)
    Release_Date = models.DateField(auto_now_add=True)
    Ratings = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.Album_Name