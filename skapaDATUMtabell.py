
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys
import random
import os


#OBS sätt första siffran in stt till dagens dagnummer för r'ätt dagtyp

stt=1

for z in range(0, 365):

   date_after_month = datetime.now()+ relativedelta(days=z)
   phdate=date_after_month.strftime('%Y-%m-%d')

   aa=phdate[0:4]
   mm=phdate[5:7]
   dd=phdate[8:10]

   print("aa",aa)
   print("mm",mm)
   print("dd",dd)



   if stt==6 or stt==7:
     dagt=1
   else:
     dagt=0
     
   if stt==7:
     stt=1
   
   stt=stt+1
   
   print(phdate,dagt)     
#
   L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO Kalender (data_date,dagtyp ) VALUES ('+ aa+mm+dd+','+str(dagt)+ ' );"'
   os.system(L)