import os
import time

# mariadb -u root -praspberry vaader -e "select * from alternativ";
# sudo mysql -u root -p

z1=0
z2=0
z4=0
z8=0
z16=0
z32=0
z64=0
z128=0
z256=0
z512=0
z1024=0
z2048=0


aantal=0

with open("output.txt", "a") as f:
 for x in range(4056):
  print(x)
  r=x
 


  if r - 2048 >= 0:
      print("ett")
      r=r-2048
      z2048=1
  else:
      print("noll")
      z2048=0

 
  if r - 1024 >= 0:
      print("ett")
      r=r-1024
      z1024=1
  else:
      print("noll")
      z1024=0



  if r - 512 >= 0:
      print("ett")
      r=r-512
      z512=1
  else:
      print("noll")
      z512=0

 
  if r - 256 >= 0:
      print("ett")
      r=r-256
      z256=1
  else:
      print("noll")
      z256=0
  
 
  if r - 128 >= 0:
      print("ett")
      r=r-128
      z128=1
  else:
      print("noll")
      z128=0
 
 
 
  if r - 64 >= 0:
      print("ett")
      r=r-64
      z64=1
  else:
      print("noll")
      z64=0
 
 
  if r - 32 >= 0:
      print("ett")
      r=r-32
      z32=1
  else:
      print("noll")
      z32=0

  if r - 16 >= 0:
      print("ett")
      r=r-16  
      z16=1
  else:
      print("noll")
      z16=0

  if r - 8 >= 0:
      print("ett")
      r=r-8 
      z8=1
  else:
      print("noll")
      z8=0

  if r - 4 >= 0:
      print("ett")
      r=r-4 
      z4=1
  else:
      print("noll")
      z4=0

  if r - 2 >= 0:
      print("ett")
      r=r-2 
      z2=1
  else:
      print("noll")
      z2=0

  if r > 0:
      print("ett")
      z1=1
  else:
      print("noll")
      z1=0

  print(".............................")


#INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (3,2,1,0);

  aantal=z1+z2+z4+z8+z16+z32+z64+z128+z256+z512+z1024+z2048

#  mariadb -u root -praspberry vaader -e "select * from alternativ";

#  L="mariadb -u root -praspberry vaader -e",aantal,",",x,",",1,",",z1,");"

  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(1)+','+str(z1)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(2)+','+str(z2)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(3)+','+str(z4)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(4)+','+str(z8)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(5)+','+str(z16)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(6)+','+str(z32)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(7)+','+str(z64)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(8)+','+str(z128)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(9)+','+str(z256)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(10)+','+str(z512)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(11)+','+str(z1024)+');"'
  os.system(L)
  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES ('+str(aantal)+','+str(x)+','+str(12)+','+str(z2048)+');"'
  os.system(L)



  L="mariadb -u root -praspberry vaader -e " + '"'+'INSERT INTO alternativR (vald,antal,altnr_id,paav1,paav2,paav3,paav4,paav5,paav6,paav7,paav8,paav9,paav10,paav11,paav12 ) VALUES ('+str(1)+','+str(aantal)+','+str(x)+','+str(z1)+','+str(z2)+','+str(z4)+','+str(z8)+','+str(z16)+','+str(z32)+','+str(z64)+','+str(z128)+','+str(z256)+','+str(z512)+','+str(z1024)+ ','+str(z2048)+');"'
  os.system(L)




#  print("INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (",aantal,",",x,",",1,",",z1,");", file=f)
#  print("INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (",aantal,",",x,",",2,",",z2,");", file=f)
#  print("INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (",aantal,",",x,",",3,",",z4,");", file=f)
#  print("INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (",aantal,",",x,",",4,",",z8,");", file=f)
#  print("INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (",aantal,",",x,",",5,",",z16,");", file=f)
#  print("INSERT INTO alternativ (antal,altnr_id ,timme,paav ) VALUES (",aantal,",",x,",",6,",",z32,");", file=f)















