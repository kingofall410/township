from django.db import models
from smart_selects.db_fields import ChainedForeignKey 

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name
    
class Muni(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    muni = ChainedForeignKey(
        Muni,
        chained_field = "state",
        chained_model_field = "state",
        show_all = False,
        auto_choose = True)