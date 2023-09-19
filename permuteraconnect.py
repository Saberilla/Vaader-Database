import os
import time



for starttimme in range(0, 24):


    nummret=0 

    for timrange in range(starttimme, starttimme + 12):

            akttimme=timrange
            nummret=nummret+1     
            if timrange >23 :
 
               akttimme = timrange- 24

            print("timme",akttimme,"minut",0,"start",starttimme,"nummer",nummret)
            L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO connect (timme,min,starttimme,nrtimme ) VALUES ('+str(akttimme)+','+str(0)+','+str(starttimme)+','+str(nummret)+');"'
            os.system(L)

            nummret=nummret+1  
            print("timme",akttimme,"minut",30,"start",starttimme,"nummer",nummret)
            L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO connect (timme,min,starttimme,nrtimme ) VALUES ('+str(akttimme)+','+str(30)+','+str(starttimme)+','+str(nummret)+');"'
            os.system(L)

 










