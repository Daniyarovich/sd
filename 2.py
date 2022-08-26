import pygsheets
import numpy as np
import requests
import math
import time
 
import sys  
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('Binance Data')
wks1 = sh.worksheet_by_title("Auto")
def newmain():
    a= []
    b= []
    c= []
    d= []
    e= []
    f= []
    g= []
    # update the sheet with array
    matrix = [] 
    stry = ""
    # share the sheet with your friend
    print()
    def insertvalue(asset, amount, tradetype, bank, row, sde):
        e = ''
        try:

            headers = {
            "Accept": "*/*",

            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com"
            }
            data = {
            "page": 1,
            "rows":1,
            "asset":asset,
            "tradeType":tradetype,
            "fiat":"RUB",
            "payTypes":[bank],
            "transAmount":amount
            }
            r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
            sp = r.text
            allinfo = sp.split('"price"');
            someinfo = allinfo[1].split('"');
            line = someinfo[1].replace('.', ',')
            
            sde.append(line)
                 
        except:
            sde.append("Пусто")
    def BUYUAH():
        insertvalue('BTC',0,'BUY','RUBfiatbalance', "C9",a)
        insertvalue('BTC',0,'BUY','RUBfiatbalance', "D9",a)
        insertvalue('BTC',0,'BUY','Advcash', "E9",a)
        insertvalue('BTC',0,'BUY','Advcash', "F9",a)
        insertvalue('BTC',0,'BUY','Payeer', "G9",a)
        insertvalue('BTC',0,'BUY','Payeer', "H9",a)
        insertvalue('BTC',0,'BUY','QIWI', "I9",a)
        insertvalue('BTC',0,'BUY','QIWI', "J9",a)
        insertvalue('BTC',0,'BUY','YandexMoneyNew', "K9",a)
        insertvalue('BTC',0,'BUY','YandexMoneyNew', "L9",a)
        insertvalue('BTC',0,'BUY','Tinkoff', "M9",a)
        insertvalue('BTC',0,'BUY','Tinkoff', "N9",a)
        insertvalue('BTC',0,'BUY','RosBank', "O9",a)
        insertvalue('BTC',0,'BUY','RosBank', "P9",a)
        insertvalue('BTC',0,'BUY','PostBankRussia', "Q9",a)
        insertvalue('BTC',0,'BUY','PostBankRussia', "R9",a)
         


     
        matrix.append(a)
        
        
        
        wks1.update_values('C9:R9', matrix ) 
        
        


         



    BUYUAH()


while True:
    newmain()
    time.sleep(10)
    pass

