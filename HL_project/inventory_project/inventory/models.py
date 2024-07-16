from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    current_stock = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    