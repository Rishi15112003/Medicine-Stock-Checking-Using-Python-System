import os
import random
import datetime
from tabulate import tabulate
import mysql.connector
def Store():
    sql="Insert into stock(Batch_no,name,date_man,date_exp,quantity,sell,balance,cost_unit)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
    acc=int(input('\nENTER THE BATCH NUMBER: '))
    nm=input('\nENTER THE THE NAME OF THE MEDICINE WITH POWER: ')
    dbs=input('\nENTER THE DATE OF MANUFACTURER(YYY-MM-DD):')
    dacc=input('\nENTER THE DATE OF EXPIRY(YYY-MM-DD):')
    quan=int(input('\nENTER THE QUANTITY OF THE IMPORTED MEDICINE:'))
    sell=0
    balance=quan
    cost=int(input'\ENTER THE COST OF THE IMPORTED MEDICINE PER UNIT: '))
    value=(acc,nm,dbs,dacc,quan,sell,balance,cost)
    try:
        mycur.execute(sql,value)
        print(nm, "ADDED TO THE STOCK'")
        mycom.commit()
    except BaseException as e:
        printIn(e)

def Search_by_Name():
    ph=input('\mENTER THE MEDICINE NAME TO SEARCH:')
    sql="select BAtch_no, name, date_man, date_exp, quantity, cost_unit from stock where name=%s"
    value =(ph,)
    mycur.execute(sql,value)
    rec=mycur.fetchone()
    if(rec==None):
        print(ph,"IS NOT AVAILABLE")
    else:
        print("BATCH NUMBER: \t",rec[0])
        print("MEDICINE NAME: \t"rec[1])
        print("DATE OF MANUFACTURE: \t",rec[2])
        print("DATE OF EXPIRY: \t", rec[3])
        print("QUANTITY STORED: \t" ,rec[4])
        print("UNIT PRICE: \t", rec[5])

def Cost_Update():
    sql="Update stock cost_unit=%s where name=%s";
    ph=input('\nENTER THE MEDICINE NAME TO CHANNEG THE COST:')
    addr=int(input('\nENTER THE NEW COST PER UNIT: '))
    value=(addr,ph)
    try:
        mycur.execute(sql,vaue)
        mycon.commit()
        print("NEW COST OF",ph,"IS Rs",addr)
    except:
        print("UNABLE TO CHANGE COST !!!!")



def Sell():
    sql="update stok set =%s, balance=%s where name=%s";
    ph=input('\nENTER THE MEDICINE NAME TO SELL:')
    addr=int(input('\nENTER THE QUANTITY TO SELL: '))
    sql2='select quantity from STOCK where name=%s'
    value2=(ph,)
    mycur.execute(sql2,value2)
    rec=mycur.fetchone()
    if(addr>rec[0]):
        print("INSUFFICIENT STOCK IN HAND !!!")
        return
    else:
        balance=rec[0]-addr
        value=(addr,balance,ph)
        try:
            mycur.ecexute(sql,value)
            mycon.commit()
            print(addr,"UNITS OF",ph,"SOLD")
            print(balance,"UNITS LEFT")
        except:
            print("UNABLE TO SELL MEDICINE!!!!")


def Available():
    ph=input('\nENTER THE MEDICINE NAME TO SEARCH:')
    sql="Select balance fees stock where name=%s"
    value=(ph,)
    mycur.execute(sql,value)
    rec=mycur.fetchone()
    if(rec==None):
        print(ph,"IS NOT AVAILABLE")
    else:
        print(rec[0],"UNITS OF",ph,"IS AVAILABLE")



def Dispose():
    sqlInsert="Insert into dispose(Batch_no,Name,date_exp,amount)values(%a,%a,%a,%a)"            
    sqlSelect="Select Batch_no,name,date_exp,balance from stock where name=%s and date_exp=%s"
    sqlDel="Delete from stock where name=%s" 

    nm=input("\nENTER THE MEDICINE NAME TO BE DISPOSED:")
    t_date=datetime.date.today()
    valueSelect=(nm,t_date)
    mycur.execute(sqlSelect,valueSelect)
    rec=mycur.fetchone()
    if(rec==None):
        print(nm,"IS NOT EXPIRED YET")
    else:
        print(nm,"IS EXPIRED")
       c=int(input("\nPRESS 1 TO DISPOSE IT:"))
       if(c==1):
        b=rec[0]
        n=rec[1]
        d=rec[2]
        am=rec[3]
        valueInsert=(b,n,d,am)
        valueDel=(n,)
        try:
            mycur.execute(sqlInsert,valueInsert)
            mycon.commit()
            print(n,"SUCCESSFULLY DISPOSED")
            mycur.execute(sqlDel,valueDel)
            mycon.commit()
        except:
            print("UNABLE TO DISPOSE MEDICINE")
       else:
        print("WARNING!!!!",nm,"MUST BE DISPOSED LATER")
        return

def Search_Dispose():
    ph=input("\nENTER THE DISPOSED MEDICINE NAME TO SEARCH:")
    sql="Select * from Dispose where Name=%s"
    value=(ph,)
    mycur.execute(sql,value)
    rec=mycur.fetchone()
    if(rec==None)
      print(ph, "IS NOT AVAILABLE")
    else:
        print("BATCH NUMBER:\t",rec[0])
        print("MEDICINE NAME:\t",rec[1])
        print("DATE OF EXPIRY:\t",rec[2])
        print("BALANCE AMOUNT:\t",rec[3])

      
def Close()
    os.system('cls')
    print('\nTHANK YOU FOR USING THE APPLICATION')
    quit()



print('            WELCOME TO MEDICINE STOCK CHECKING SYSTEM           \n\n')
while(True):
   os.system('cls')
   print('\n\nPRESS 1 TO ADD NEW MEDICINE')
   print('PRESS 2 TO SEARCH A MEDICINE BY NAME')
   print('PRESS 3 TO UPDATE MEDICINE COST')
   print('PRESS 4 TO SELL MEDICINE')
   print('PRESS 5 TO CHECK AVAILABILITY')
   print('PRESS 6 TO DISPOSE EXPIRED MEDICINE')
   print('PRESS 7 TO SEARCH EXPIRED MEDICINE BY NAME')
   print('PRESS 8 TO CLOSE THE APPLICATION')
   choice=int(input('ENTER YOUR CHOICE: '))
   if(choice==1):
     os.system('cls')
     Store()
   elif(choice==2):
      os.system('cls')
      Search_by_Name()
   elif(choice==3):
      os.system('cls')
      Cost_Update()
   elif(choice==4):
      os.system('cls')
      Sell()
   elif(choice==5):
      os.system('cls')
      Available()
   elif(choice==6):
      os.system('cls')
      Dispose()
   elif(choice==7):
      os.system('cls')
      Search_Dispose()
   elif(choice==8):
      Close()
   else:
    print("Please enter a valid choice.")   
                 








            
    
