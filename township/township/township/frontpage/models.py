from django.db import models
from smart_selects.db_fields import ChainedForeignKey 

# state is highest level
class State(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name
    
    def fully_qualified(self):
        return self.name
    
#county/parish.borough is directly under state
#https://en.wikipedia.org/wiki/County_(United_States)
class County(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def fully_qualified(self):
        return self.state.fully_qualified()+", "+self.name
    
#TBD what happens when a municipality is part of multiple counties (NYC).  
#Special case, doesn't matter for now    
class Muni(models.Model):
    name = models.CharField(max_length=200)
    county = models.ForeignKey(County, on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return self.name
    
    def fully_qualified(self):
        return self.county.fully_qualified()+", "+self.name
    
class Location(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    county = ChainedForeignKey(
        County,
        chained_field = "state",
        chained_model_field = "state",
        show_all = False,
        auto_choose = True,
        default=0)
        
    muni = ChainedForeignKey(
        Muni,
        chained_field = "county",
        chained_model_field = "county",
        show_all = False,
        auto_choose = True)