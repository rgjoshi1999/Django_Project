from django.db import models

# Create your models here.

class Feedback(models.Model):
    username=models.CharField(max_length=30)
    created_data=models.DateTimeField(auto_now_add=True)
    feedback=models.TextField()


course_ch = (("Full Stack Java", "Full Stack Java"),
                 ("Full Stack Python", "Full Stack Python"),
                 ("Data Science", "Data Science"),
                 ("AWS", "AWS"),
                 ("MERN Stack","MERN Stack"),
                 ("Spoken English","Spoken English"),
                 ("Data Analytics","Data Analytics"),
                 ("DevOps","DevOps"))

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    Course = models.CharField(max_length=100, choices=course_ch,default=' ')
    #message = models.CharField(max_length=50)



    def __str__(self):
        return self.name
'''
class Course(models.Model):
    name = models.CharField(max_length=255)'''

'''
class Payment(models.Model):
    amount = models.IntegerField()
    card_number = models.CharField(max_length=10)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvc = models.IntegerField()
'''