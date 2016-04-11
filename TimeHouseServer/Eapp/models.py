from django.db import models

# Create your models here.
class UserOption(models.Model):
    """
    用户选择
    """
    ip = models.CharField(max_length=20)
    choise = models.BooleanField()
    choose_time = models.DateTimeField()