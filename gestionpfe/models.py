from django.db import models
from django.contrib.auth.models import User


class DemandeStageMonome(models.Model):
    userun=models.OneToOneField(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)  
    ncin=models.CharField(max_length=8) 
    parcours=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    
    
     
    def __str__ (self):
        return self.nom.capitalize()
    
    
    
class DemandeStageBinome(models.Model):
    binome1=models.OneToOneField(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)  
    ncin=models.CharField(max_length=8) 
    parcours=models.CharField(max_length=255) 
    email=models.EmailField(max_length=255)
    nom2=models.CharField(max_length=255)
    prenom2=models.CharField(max_length=255)  
    ncin2=models.CharField(max_length=8) 
    parcours2=models.CharField(max_length=255) 
    email2=models.EmailField(max_length=255) 
    
    def __str__ (self):
        return self.nom.capitalize()
    
     
        

    
    

    
    

    
