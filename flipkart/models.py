from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PriceDrop(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name="Pricedrop", null=True)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    curr_price = models.DecimalField(max_digits=10000, decimal_places=2)
    #changed_price = models.DecimalField(decimal_places=2)
    added_at = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
