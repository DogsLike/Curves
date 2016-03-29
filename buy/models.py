from django.db import models

# Create your models here.
class BuyDiamond(models.Model):
	"""docstring for BuyDiamond"""
	diamond_total_num = models.IntegerField(default=0)
		

class DiamondTrade(models.Model):
	"""docstring for DiamondTrade"""
	ip = models.CharField(max_length=50)
	diamond_num = models.IntegerField(default=0)
	trade_date = models.DateTimeField('trade date')



		