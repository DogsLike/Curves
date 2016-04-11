#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import BuyDiamond,DiamondTrade
import simplejson
import hashlib
import unicodedata
# Create your views here.
def index(request):
	return HttpResponse("Hello World!")

def buyGold(request, num):
	res = "not"
	if num == "5":
		res = "ok" + "_50"
		tradeDataHandler(5)
	if num == "48":
		res = "ok" + "_500"
		tradeDataHandler(48)
	if num == "288":
		res = "ok" + "_3000"
		tradeDataHandler(288)
	return HttpResponse(res)


def tradeDataHandler(num):
	if not BuyDiamond.objects.all():
		buy = BuyDiamond()
		buy.save()
	trade = DiamondTrade(diamond_num = num,trade_date = timezone.now())
	trade.save()
	buy = BuyDiamond.objects.get(id=1)
	buy.diamond_total_num += num
	buy.save()

def login_game(request): 
    #contributed by 杜可夫 duke.cliff@icloud.com
    html = '' 
    ret = 'login failed' 
    private_key = '6A1C6E8C94DE8A829E2CD9387F0DCC9E' 
    #loginCheckUrl = 'http://oauth.anysdk.com/api/User/LoginOauth/'
    if request.method == 'POST': 
        post_key = request.POST.get('private_key', '') 
        if post_key == private_key: 
            post_data = {} 
            post_data = request.POST 
            anysdk_conn = httplib.HTTPConnection('oauth.anysdk.com') 
            headers = {"Content-Type": "application/x-www-form-urlencoded"} 
            post_str = '' 
            first = True 
            for key, value in post_data.items(): 
                if not first: 
                    post_str += '&' 
                first = False 
                post_str += key + '=' + value 
            anysdk_conn.request("POST", '/api/User/LoginOauth/', post_str, headers) 
            response = anysdk_conn.getresponse() 
            if response.status == 200: 
                content = response.read() 
                #print "any_sdk login result:", content
                resp_dict = json.loads(content) 
                resp_dict['ext'] = 'game_tag' 
                ret = resp_dict 
    html = simplejson.dumps(ret, ensure_ascii = False) 
    response = HttpResponse(html)  
    return response 

def anysdk_payment(request):
    '''
    contributed by 杜可夫 (duke.cliff@icloud.com)
    '''
    html = 'OK'
    if request.method == 'POST':
        #private_data may be refererd to as your own tracking number
        private_data = request.POST.get('private_data', '')
        server_id = request.POST.get('server_id', '')
        trade_status = request.POST.get('pay_status', '')
        channel = request.POST.get('channel_number', '')
        user_id = request.POST.get('user_id', '')
        total_fee = float(request.POST.get('amount', '0.0'))
        sign = request.POST.get('sign', '')
        private_key = '6A1C6E8C94DE8A829E2CD9387F0DCC9E'
        if trade_status == '1':
            validated_order = False
            temp_list = []
            for key, value in request.POST.items():
                if key != 'sign':
                    temp_list.append([key, value])
            temp_list = sorted(temp_list, cmp=lambda x,y: cmp(x[0], y[0]))
            raw_str = ''
            for item in temp_list:
                raw_str = raw_str + item[1]
            md5_raw_str = hashlib.md5(raw_str).hexdigest().lower()
            local_sign = hashlib.md5(md5_raw_str + private_key).hexdigest().lower()
            if local_sign == sign:
                validated_order = True
            if validated_order:
                #支付完成，并且合法，更新支付状态信息或者通知游戏服务器更新数据...
                pass
    response = HttpResponse(html)
    return response

