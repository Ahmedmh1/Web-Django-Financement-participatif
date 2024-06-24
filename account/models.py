from django.db import models

# Create your models here.


class Project(models.Model):
    Nameproject = models.CharField(max_length=200)
    Streetaddress = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    Description = models.CharField(max_length=700)
    image=models.ImageField(upload_to='crops_images/',null=True,blank=True)
    class Meta:
        db_table='Project'
        
    def __str__(self):
        return self.Nameproject