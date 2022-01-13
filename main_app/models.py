from django.db import models

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
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