from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import BuyDiamond,DiamondTrade
# Create your views here.

def index(request):
	return HttpResponse("Hello World!")

def buyGold(request, num):
	res = "not"
	if num=="5":
		res = "ok"+"_50"
		tradeDataHandler(50)
	if num=="48":
		res = "ok"+"_500"
		tradeDataHandler(500)
	if num=="288":
		res = "ok"+"_3000"
		tradeDataHandler(3000)
	return HttpResponse(res)


def tradeDataHandler(num):
	if not BuyDiamond.objects.all():
		buy = BuyDiamond()
		buy.save();
		print("~~~~~~~~")
	trade = DiamondTrade(diamond_num = num,trade_date = timezone.now())
	trade.save();
	buy = BuyDiamond.objects.get(id=1)
	buy.diamond_total_num += num
	buy.save()
