from django.db import models


# Create your models here.

class Qustion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice (models.Model):
    question =models.ForeignKey(Qustion,on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
