from django.db import models
from django.urls import reverse

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    size = models.CharField(
        max_length=1,
        choices=SIZES,
        default=SIZES[0][0]
    )
    age = models.IntegerField()
    description= models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dogs_detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0],
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"