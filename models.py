from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=70)    
#     email = models.EmailField(max_length = 100)
#     password = models.CharField(max_length=100)

class DailyReport(models.Model):
    name = models.CharField(max_length=70)    
    email = models.EmailField(max_length = 100)
    assigned_work = models.CharField(max_length=100)
    completed = models.CharField(max_length=100)
    pending = models.CharField(max_length=100)
    