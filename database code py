import mysql.connector as sql
from time import sleep

conn=sql.connect(host = 'localhost',user='root',passwd='1234567890')
c1=conn.cursor()
if conn.is_connected():
    c1.execute("create database if not exists rail;")
    
    c1.execute('use rail;')

    c1.execute('create table if not exists traindetail (tname varchar(50), tnum int(6) primary key, src varchar(50), des varchar(50), ac1 int(5), ac2 int(5), ac3 int(5), slp int(5))')

    c1.execute('create table if not exists passengers (pname varchar(20), age int(3), trainno int(6), noofpas int(3), cls varchar(4), amt int(6), status varchar(10), pnrno int(6))')

    c1.execute('insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values("Ernakulam JN Nizamuddin Duronto Express",12283,12,48,256,504)')




    c1.execute('insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values("Trivandrum Central Rajdhani",12432,36,240,704,NULL)')

    c1.execute('insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values("Sampark Kranthi Express",12217,18,96,384,432)')

    c1.execute('insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values("Rapthisagar Express",12512,18,96,448,432)')

    c1.execute('insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values("Gurvayur Chennai Egmore Express", 16128,NULL,48,128,720)')

    c1.execute('insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values("Swarna Jayanti SF Express",12644,NULL,48,448,648)')

    conn.commit()

    print('\n\n\n\n\n-------------Database successfully created-------------')
    sleep(3)
