from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=225)
    fee=models.IntegerField()

    def __str__(self):
        return self.course_name

class Student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    std_name=models.CharField(max_length=255)
    std_address=models.TextField()
    std_age=models.IntegerField()
    std_email=models.EmailField()
    joining_date=models.DateField()    