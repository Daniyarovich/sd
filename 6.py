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
        insertvalue('RUB',0,'BUY','RUBfiatbalance', "C17",a)
        insertvalue('RUB',0,'SELL','RUBfiatbalance', "D17",a)
        insertvalue('RUB',0,'BUY','Advcash', "E17",a)
        insertvalue('RUB',0,'SELL','Advcash', "F17",a)
        insertvalue('RUB',0,'BUY','Payeer', "G17",a)
        insertvalue('RUB',0,'SELL','Payeer', "H17",a)
        insertvalue('RUB',0,'BUY','QIWI', "I17",a)
        insertvalue('RUB',0,'SELL','QIWI', "J17",a)
        insertvalue('RUB',0,'BUY','YandexMoneyNew', "K17",a)
        insertvalue('RUB',0,'SELL','YandexMoneyNew', "L17",a)
        insertvalue('RUB',0,'BUY','Tinkoff', "M17",a)
        insertvalue('RUB',0,'SELL','Tinkoff', "N17",a)
        insertvalue('RUB',0,'BUY','RosBank', "O17",a)
        insertvalue('RUB',0,'SELL','RosBank', "P17",a)
        insertvalue('RUB',0,'BUY','PostBankRussia', "Q17",a)
        insertvalue('RUB',0,'SELL','PostBankRussia', "R17",a)
         


     
        matrix.append(a)
        
        
        
        wks1.update_values('C17:R17', matrix ) 
        
        


         



    BUYUAH()


while True:
    newmain()
    time.sleep(10)
    pass

