from django.db import models

# Create your models here.
class studentmodel(models.Model):
    student_name=models.CharField(max_length=30)
    dateofbirth=models.DateField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    maths=models.IntegerField()
    computerscience=models.IntegerField()
    percentage=models.FloatField()
