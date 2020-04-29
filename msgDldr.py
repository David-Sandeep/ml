# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:42:21 2019

@author: David Sandeep
"""

import os
import urllib.request as ur

keyss={1:'genesis',2:'Leviticus',3:'Job',4:'Proverbs',
       5:'Ecclesiastes&SongOfSolomon',6:'Matthew',7:'Mark',8:'Luke',9:'John',
       10:'Romans',11:'Revelation'}
def loar(df):
   if df==1:

      try:
         os.mkdir("genesis")
      except:
         pass
      print("Downloading.... \ngenesis book messages...")

      for i in range(1,57):
          try:
              u="http://uecf.net/messages/RRK/"+str(i)+".mp3"
              fullfilename = os.path.join("genesis",str(i)+".mp3" )
              ur.urlretrieve(u,fullfilename)
              print(str(i)+".mp3"+" downloaded! \n")
          except Exception:
              pass

      print(keyss[df]+" book messages completed downloading !!")
      print("check this path!!-->"+os.getcwd()+"\\"+keyss[df])

   else:

      try:
         os.mkdir(keyss[df])
      except:
         pass

      print("Downloading.... \n"+keyss[df]+" book messages...")

      for i in range(1,66):
          try:
              u="http://uecf.net/messages/RRK/"+keyss[df]+"/"+str(i)+".mp3"
              fullfilename = os.path.join(keyss[df],str(i)+".mp3" )
              ur.urlretrieve(u,fullfilename)
              print(str(i)+".mp3"+" downloaded! \n")
          except Exception:
              pass

      print(keyss[df]+" book messages completed downloading !!")
      print("check this path!!-->"+os.getcwd()+"\\"+keyss[df])

while True:
   print("\n")
   print(keyss)
   print("\n{0.exit()}\n")

   try:
      df=int(input("Enter serial no . to download.."))
      if df>=1 and df<=12:
         loar(df)
      elif df==0:
         break

      else:
         print("Please enter b/w serial numbers!!):")


   except:
      print("Please enter b/w serial numbers!!):")
      print("tQ!!")
