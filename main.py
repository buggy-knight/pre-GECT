import mysql.connector
import os
from time import sleep, localtime, ctime
import prettytable
import csv
from pyautogui import alert
from sys import exit
from tkinter import filedialog

mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234567890",database="rail");
mycursor=mydb.cursor()

#Main Screen
def railresmenu():
    print("\n------RAILWAY RESERVATION SYSTEM-----\n")
    print("1. Train Details")
    print("2. Reservation of Ticket")
    print("3. Cancellation of Ticket")
    print("4. Display PNR status")
    print("5. Print Ticket")
    print('6. Export Reservation Chart')
    print("7. Quit")
              
    n=input("\nEnter your choice: ")
    if(n=='1'):
        sleep(0.2)
        traindetail()
        
    elif(n=='2'):
        sleep(0.2)
        reservation()
        
    elif(n=='3'):
        sleep(0.2)
        cancel()

    elif(n=='4'):
        sleep(0.2)
        displayPNR()

    elif(n=='5'):
        export2txt()

    elif(n=='6'):
        export2CSV()

    elif(n=='7'):
        sleep(0.2)

        alert('Thank you for visiting this portal.', title='Railway Reservation System')

        exit()
        
    else:
        print("\nInvalid Choice. Returning to Reservation Menu")

        sleep(0.3)
        railresmenu()
                 
#Train Details Window               
def traindetail():
    sleep(0.3)
    print("\nTRAIN DETAILS")
    print('—————————————')

    while True:
        l=[]
        name=input("\nEnter Train name: ")
        l.append(name)
        tnum=int(input("Enter Train number: "))
        l.append(tnum)
        ac1=int(input("Enter Number of AC 1 class seats: "))
        l.append(ac1)

        ac2=int(input("Enter Number of AC 2 class seats: "))
        l.append(ac2)

        ac3=int(input("Enter Number of AC 3 class seats: "))
        l.append(ac3)

        slp=int(input("Enter Number of sleeper class seats: "))
        l.append(slp)

        train=(l)
        sql="insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,train)
        mydb.commit()

        print("Insertion completed")

        ch=input("Do you want to insert more train details?(y/n) ")


        if ch[0].lower() != 'y':
            break

    sleep(0.2)
    print('\nReturning to Main menu...')
    print('\n' *3)
    sleep(0.3)

    railresmenu()


#Reservation Window

def reservation():
    sleep(0.3)
    mycursor.execute('select pnrno from passengers;')
    data = mycursor.fetchall()
    if len(data) == 0:
        pnr=1024
    else:
        pnr=data[-1][0]+1
    l1=[ ]
    print('\nTICKET RESERVATION PORTAL')
    print('—————————————————————————')
    pname=input("\nEnter passenger name: ")
    l1.append(pname)
    age=input("Enter age of passenger: ")
    l1.append(age)
    trainno=input("Enter train number: ")
    l1.append(trainno)
    np=int(input("Enter number of passengers: "))
    l1.append(np)


    print("\nSelect a class you would like to travel in\n")
    print("1.AC FIRST CLASS")
    print("2.AC SECOND CLASS")
    print("3.AC THIRD CLASS")
    print("4.SLEEPER CLASS")
    sleep(0.2)
    cp=int(input("\nEnter your choice: "))
    if(cp==1):
        amount=np*1000
        cls='ac1'

    elif(cp==2):
        amount=np*800
        cls='ac2'
    elif(cp==3):
        amount=np*500
        cls='ac3'
    else:
        amount=np*350
        cls='slp'
    l1.append(cls)
    alert('Ticket Reserved successfully.\nTotal Amount to be paid is: '+str(amount)+'.00\n Your PNR number is: '+str(pnr), title='Railway Reservation System')
    l1.append(amount)
    sts='conf'
    l1.append(sts)
    l1.append(pnr)
    train1=(l1)

    sql="insert into passengers(pname,age,trainno,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"


    mycursor.execute(sql,train1)
    mydb.commit()
    print("\nInsertion completed")
    print("\nReturning to Main menu\n")
    sleep(0.3)
    railresmenu()



    

#Cancellation Window
def cancel():
    print("\nTICKET CANCELLATION WINDOW")
    print('——————————————————————————')
    pnr=input("Enter PNR for cancellation of Ticket: ")
    pn=(pnr,)
    sql="update passengers set status='cancelled' where pnrno=%s"
    mycursor.execute(sql,pn)
    mydb.commit()
    print("\nCancellation completed")
    sleep(0.2)
    print("\nReturning to Main menu\n\n")
    sleep(0.3)    
    railresmenu()
    

#PNR Check
def displayPNR():
    print("\nPNR STATUS CHECK")
    print('————————————————')
    pnr=input("Enter PNR number: ")
    pn=(pnr,) 

    sql="select * from passengers where pnrno=%s"
    mycursor.execute(sql,pn)
    res=mycursor.fetchall()
    table = prettytable.PrettyTable(['Passenger Name','Age','Train No.', 'No of Passengers','Category','Ticket Amount','PNR Status', 'PNR Number'])
    table.add_rows(res)
    print(table)
    sleep(0.2)

    print("Returning to Main menu...")
    sleep(0.3)
    railresmenu()

#Exporting Reservation Chart
def getTime():
    t = list(localtime())
    r = ''
    for i in range(len(t)-2):
        r+=str(t[i])
    return r

def export2CSV():
    sql = 'select * from passengers;'
    mycursor.execute(sql)
    data=mycursor.fetchall()
    header = [['Passenger Name','Age','Train No.', 'No of Passengers','Category','Ticket Amount','PNR Status', 'PNR Number']]
    path = filedialog.askdirectory()

    if path == '':
        print('Returning to Main Menu...')
        sleep(0.3)
        railresmenu()
    fname = path+r'\export'+getTime()
    fname+='.csv'
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(header+data)
    os.startfile(fname)
    sleep(0.33)
    print('Returning to Main Menu...')
    sleep(0.3)
    railresmenu()

#Exporting Ticket
def export2txt():
    pnr=input("Enter PNR number: ")
    pn=(pnr,) 
    sql="select * from passengers where pnrno=%s"
    mycursor.execute(sql,pn)
    res=mycursor.fetchall()

    table = prettytable.PrettyTable(['Passenger Name','Age','Train No.', 'No of Passengers','Category','Ticket Amount','PNR Status', 'PNR Number'])

    table.add_rows(res)
    path = filedialog.askdirectory()
    if path == '':
        print('Returning to Main Menu...')
        sleep(0.3)
        railresmenu()

    fname = path+r'\ticket '+getTime()
    fname+='.txt'
    with open(fname, 'w') as f:
            f.write('RAILWAY RESERVATION SYSTEM\n\n')
            f.write(ctime()+'\n\n')
            f.write(str(table))
    os.startfile(fname)
    sleep(0.33)
    print('Returning to Main Menu...')
    sleep(0.3)
    railresmenu()

railresmenu()
