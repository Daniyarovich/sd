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
        insertvalue('BUSD',0,'BUY','RUBfiatbalance', "C11",a)
        insertvalue('BUSD',0,'BUY','RUBfiatbalance', "D11",a)
        insertvalue('BUSD',0,'BUY','Advcash', "E11",a)
        insertvalue('BUSD',0,'BUY','Advcash', "F11",a)
        insertvalue('BUSD',0,'BUY','Payeer', "G11",a)
        insertvalue('BUSD',0,'BUY','Payeer', "H11",a)
        insertvalue('BUSD',0,'BUY','QIWI', "I11",a)
        insertvalue('BUSD',0,'BUY','QIWI', "J11",a)
        insertvalue('BUSD',0,'BUY','YandexMoneyNew', "K11",a)
        insertvalue('BUSD',0,'BUY','YandexMoneyNew', "L11",a)
        insertvalue('BUSD',0,'BUY','Tinkoff', "M11",a)
        insertvalue('BUSD',0,'BUY','Tinkoff', "N11",a)
        insertvalue('BUSD',0,'BUY','RosBank', "O11",a)
        insertvalue('BUSD',0,'BUY','RosBank', "P11",a)
        insertvalue('BUSD',0,'BUY','PostBankRussia', "Q11",a)
        insertvalue('BUSD',0,'BUY','PostBankRussia', "R11",a)
         


     
        matrix.append(a)
        
        
        
        wks1.update_values('C11:R11', matrix ) 
        
        


         



    BUYUAH()


while True:
    newmain()
    time.sleep(10)
    pass

