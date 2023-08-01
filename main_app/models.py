from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    weight = models.IntegerField()
    diet = models.TextField(max_length=250)
    vaccinated = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    
GRADES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('F', 'F'),
)

class ReportCard(models.Model):
    date = models.DateField()
    behavior = models.TextField(max_length=250)
    summary = models.TextField(max_length=250)
    grade = models.CharField(
        max_length=1,
        choices=GRADES,
        default=GRADES[0][0]
    )
    fed = models.BooleanField(default=True)

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_grade_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']