from django.db import models

# Create your models here.

# to add bunch of cities name in the table 
# this models.Model will create columns in the database 
# as in this case it creates only one column i.e. name

class City(models.Model):
    name = models.CharField(max_length=25) # to store the cities we are creating in a single column

    # define string method on it as this will convert object into string

    def __str__(self):
        return self.name

    # also define meta class for making single name i.e.city to cities
    
    class Meta:
        verbose_name_plural = 'cities'

class Season(models.Model):
    Season1 = models.CharField(max_length=30)
    Sid = models.IntegerField(max_length=5)

    def __str__(self):
        return self.Season1
