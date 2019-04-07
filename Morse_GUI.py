from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setwarnings(False)

##LED
ledred = LED(15)


##GUI
win=Tk()
win.title("LED Toggler")
myfont=tkinter.font.Font(family='Helvetica', size=12, weight="bold")

##Functions

def ShortBlink():
    ledred.on()
    time.sleep(0.5)
    ledred.off()
    time.sleep(1)

def LongBlink():
    ledred.on()
    time.sleep(2)
    ledred.off()
    time.sleep(1)   
        
def a():
    ShortBlink()
    LongBlink()

def b():
    LongBlink()
    ShortBlink()
    ShortBlink()
    ShortBlink()            

def c():
    LongBlink()
    ShortBlink()
    LongBlink()
    ShortBlink()

def d():
    LongBlink()
    ShortBlink()
    ShortBlink()
            
def e():
    ShortBlink()

def f():
    ShortBlink()
    ShortBlink()
    LongBlink()
    ShortBlink()

def g():
    LongBlink()
    LongBlink()
    ShortBlink()
    
def h():
    ShortBlink()
    ShortBlink()
    ShortBlink()
    ShortBlink()

def i():
    ShortBlink()
    ShortBlink()

def j():
    ShortBlink()
    LongBlink()
    LongBlink()
    LongBlink()

def k():
    LongBlink()
    ShortBlink()
    LongBlink()

def l():
    ShortBlink()
    LongBlink()
    ShortBlink()
    ShortBlink()

def m():
    LongBlink()
    LongBlink()

def n():
    LongBlink()
    ShortBlink()

def o():
    LongBlink()
    LongBlink()
    LongBlink()

def p():
    ShortBlink()
    LongBlink()
    LongBlink()
    ShortBlink() 

def q():
    LongBlink()
    LongBlink()
    ShortBlink()
    LongBlink()  

def r():
    ShortBlink()
    LongBlink()
    ShortBlink()  

def s():
    ShortBlink()
    ShortBlink()
    ShortBlink()

def t():
    LongBlink()

def u():
    ShortBlink()
    ShortBlink()
    LongBlink()

def v():
    ShortBlink()
    ShortBlink()
    ShortBlink()
    LongBlink()

def w():
    ShortBlink()
    LongBlink()
    LongBlink()
            
def x():
    LongBlink()
    ShortBlink()
    ShortBlink()
    LongBlink()

def y():
    LongBlink()
    ShortBlink()
    LongBlink()
    LongBlink()

def z():
    LongBlink()
    LongBlink()
    ShortBlink()
    ShortBlink()

def MorseCode():
    word_to_morse=word.get()
    
    charactersNumber=0
    
    for x in word_to_morse:
        charactersNumber=charactersNumber+1
        
    if(charactersNumber<=12):
        for ch in word_to_morse:
            if(ch.lower()=='a'):
                a()
            elif(ch.lower()=='b'):
                b()
            elif(ch.lower()=='c'):
                c()
            elif(ch.lower()=='d'):
                d()
            elif(ch.lower()=='e'):
                e()
            elif(ch.lower()=='f'):
                f()
            elif(ch.lower()=='g'):
                g()
            elif(ch.lower()=='h'):
                h()
            elif(ch.lower()=='i'):
                i()
            elif(ch.lower()=='j'):
                j()
            elif(ch.lower()=='k'):
                k()
            elif(ch.lower()=='l'):
                l()
            elif(ch.lower()=='m'):
                m()
            elif(ch.lower()=='n'):
                n()
            elif(ch.lower()=='o'):
                o()
            elif(ch.lower()=='p'):
                p()
            elif(ch.lower()=='q'):
                q()
            elif(ch.lower()=='r'):
                r()
            elif(ch.lower()=='s'):
                s()
            elif(ch.lower()=='t'):
                t()
            elif(ch.lower()=='u'):
                u()
            elif(ch.lower()=='v'):
                v()
            elif(ch.lower()=='w'):
                w()
            elif(ch.lower()=='x'):
                x()
            elif(ch.lower()=='y'):
                y()
            elif(ch.lower()=='z'):
                z()
            time.sleep(0.25)
                
    else:
        print("Please enter word that is less than 12 characters")

def close():
    RPi.GPIO.cleanup()
    win.destroy()

##Buttons
    
word=StringVar()

mylabel=Label(win,text='Please enter a word:').grid(row=0)
    
morseButton=Button(win, text='Morse', font = myfont, command= MorseCode,bg='green',height=1,width=6)
morseButton.grid(row=1,column=1)

textBox=Entry(win, font = myfont,textvariable=word, bg='white')
textBox.grid(row=0,column=1)  

exitButton=Button(win, text='Exit', font = myfont, command=close, bg='red',height=1,width=6)
exitButton.grid(row=2,column=1)




win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()


