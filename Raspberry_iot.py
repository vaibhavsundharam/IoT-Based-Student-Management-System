import mysql.connector
import RPi.GPIO as GPIO
import time
rs= 7
en =8
d0=25
d1=24
d2=23
d3=18
r1=2
r2=3
r3=14
r4=15
global x1
#low = False
#high = True
old_notice=""
old_time=""
def ini():
lcdcmd(0x33)
    lcdcmd(0x32)
    lcdcmd(0x01)
    lcdcmd(0x28)
    lcdcmd(0x80)
    lcdcmd(0x0e)
    lcdcmd(0x06)
def lcdcmd(value):
    GPIO.output(rs,False)    
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)    
    if value&0x10==0x10:
        GPIO.output(d0,True)
    if value&0x20==0x20:
    GPIO.output(d1,True)
    if value&0x40==0x40:
        GPIO.output(d2,True)
    if value&0x80==0x80:
        GPIO.output(d3,True)
    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)    
    if value&0x01==0x01:
        GPIO.output(d0,True)
    if value&0x02==0x02:
        GPIO.output(d1,True)
    if value&0x04==0x04:
        GPIO.output(d2,True)
    if value&0x08==0x08:
        GPIO.output(d3,True)
    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)
    def lcddata(value):
    GPIO.output(rs,True)    
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
GPIO.output(d3,False)    
    if value&0x10==0x10:
        GPIO.output(d0,True)
    if value&0x20==0x20:
        GPIO.output(d1,True)
    if value&0x40==0x40:
        GPIO.output(d2,True)
    if value&0x80==0x80:
        GPIO.output(d3,True)
    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)    
    if value&0x01==0x01:
GPIO.output(d0,True)
    if value&0x02==0x02:
        GPIO.output(d1,True)
    if value&0x04==0x04:
        GPIO.output(d2,True)
    if value&0x08==0x08:
        GPIO.output(d3,True)
GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)
def stri(message):
for i in range (len(message)):        
        lcddata(ord(message[i]))
def received_notice():
db=mysql.connector.connect(host='192.168.43.87', database='student',user='root',password='123456')
    cur=db.cursor()
cmd="select notice from notice"
    cur.execute(cmd)
    x=cur.fetchone()
    x=x[0]
    db.commit()
    cur.close()
    db.close()
    return x
i=0
def received_timetable():
    global i
    db=mysql.connector.connect(host='192.168.43.87', database='student',user='root',password='123456')
    cur=db.cursor()
    cmd="select  * from time"
    cur.execute(cmd)
    y=cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    cs=y[i][2]
    tm=y[i][3]
    fc=y[i][4]
    i=i+1
    if (i>len(y)):
        i=0
    return(cs,tm,fc)
if __name__ == '__main__':

    try :
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rs,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)
        GPIO.setup(d0,GPIO.OUT)
        GPIO.setup(d1,GPIO.OUT)
        GPIO.setup(d2,GPIO.OUT)
        GPIO.setup(d3,GPIO.OUT)        
        GPIO.setup(r1,GPIO.IN)
        GPIO.setup(r2,GPIO.IN)
        GPIO.setup(r3,GPIO.IN)
        GPIO.setup(r4,GPIO.IN)
        ini()
        lcdcmd(0x81)
        stri("CLS")
        lcdcmd(0x86)
        stri("TIME")
        lcdcmd(0x8c)
        stri("FACULTY")
        while(True):
            count=''
notice=received_notice()
            (cs,tm,fc)=received_timetable()
            print(cs,tm,fc)
            lcdcmd(0xc1)
            stri(str(cs))
            lcdcmd(0xc6)
            stri(str(fc))
            lcdcmd(0xcc)
stri(str(tm))
            lcdcmd(0x94)
            stri("Nc:")
            lcdcmd(0x97)
            stri(str(notice))
            if(GPIO.input(2)==True and GPIO.input(3)==False andGPIO.input(14)==False and GPIO.input(15)==False):#8
                count='8'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==False and GPIO.input(14)==False and GPIO.input(15)==True):# 7
                count='7'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==False and GPIO.input(14)==True and GPIO.input(15)==False):#6
                count='6'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==False and GPIO.input(14)==True and GPIO.input(15)==True): #5
                count='5'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==True and GPIO.input(14)==False and GPIO.input(15)==False): #4
                count='4'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==True and GPIO.input(14)==False and GPIO.input(15)==True): #3
                count='3'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==True and GPIO.input(14)==True and GPIO.input(15)==False): #2
                count='2'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)                
            elif(GPIO.input(2)==True and GPIO.input(3)==True and GPIO.input(14)==True and GPIO.input(15)==True): # 1
                count='1'
                print(count)
                lcdcmd(0xd4)
                stri("SC:")
                lcdcmd(0xd7)
                stri(count)     
db=mysql.connector.connect(host='localhost',database='student',user='root',password='123456')
cur=db.cursor()
'''if(old_notice!= notice):
                old_notice=notice
                stri(notice)
                #stri(x1)
                print(notice)
            else:                pass'''
    except KeyboardInterrupt:
        pass



