from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_ahora = False , auto_ahora_añadir = False)
    time = models.IntegerField()  
 