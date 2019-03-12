import time
from linebot import LineBotApi
from linebot.models import TextSendMessage
import Pageb as Pageb



channel_access_token='das1jTqlXYx2852SNfKRGeYbBmXPZnsZAfv+ivD4FimwqeVB9Rx4jD9tY6nSY6MS3bJB5EX02yITbEjLdBvY6G/RXa0wuv6NBZMZhpx59XjT2v+lR4+pL29jQ0MCCe2WySx+W+Co+WNzIEz/XEXA7wdB04t89/1O/w1cDnyilFU='
user_id2 = 'U118d444acaaee88036c05361815f23bd'  #我的
user_id1 = 'U00bef3d6698992d2efde78386775e329'  #瀚的
#user_id = [U118d444acaaee88036c05361815f23bd, U00bef3d6698992d2efde78386775e329]
line_bot_api = LineBotApi(channel_access_token)

quote_name = ['全職法師']
quote_url = ['https://www.ptwxz.com/bookinfo/7/7197.html']
quote_no = []


for i in range(len(quote_name)):
    a = Pageb.Pageb(quote_name[i],quote_url[i])
    quote_no.append(a)
    
line_bot_api.multicast([user_id1, user_id2], TextSendMessage(text='機器人啟動'))
                          
while True:
    for i in range(len(quote_no)):
        now = quote_no[i].get_pageb()
        if now.get("title") != quote_no[i].title: 
            line_bot_api.multicast([user_id1, user_id2], TextSendMessage(text= quote_name[i] + ':  新的一集已經更新了唷!!'))
            line_bot_api.multicast([user_id1, user_id2], TextSendMessage(text = now.get("title") +" : "+ now.get("href") ))
            old = now.get("href")  
        else:
            print ("尚未更新喔")
    time.sleep(1800)            
