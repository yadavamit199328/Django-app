from django.db import models

# Create your models here.
class Start(models.Model):
    name = models.CharField(max_length = 100)
    coupon = models.CharField(max_length = 100)

    def __str__(self):
        return "{} {}".format(self.name,self.coupon)
class Phoneno(models.Model):
    phoneno = models.CharField(max_length = 10)

    def __str__(self):
        return "{}".format(self.phoneno)