#icsd18174 
#Exercise 1 Assingment 3 
from datetime import datetime
import urllib.request  # the lib that handles the url stuff
import time                    #import the time library this will help us calculate the differences between two dates
import pathlib                                   #import the pathlib library
import os                      #for presentation purposes


print("Loading...")            #for presentation purposes

file = pathlib.Path("dict.txt")                   
if file.exists ():                           #checks if the file exists or else it creates a new one 
    print ("File exist")
else:
    print ("Creating new File.")
    f=open("dict.txt",mode='w',encoding='utf-8')
open('dict.txt', 'w').close()                                    #to not rewritte the same stuff everytime it opens the file and the file already exists
f = open("dict.txt",mode = 'a',encoding = 'utf-8')              #open a stream for appendance 
r = open("dict.txt",mode = 'r',encoding = 'utf-8')              #open a stream for reading 

Countries =[]                                        #list to store the countries
class country:                                     #class that creates onjects with the required information for a country
    dailySick = 0
    name =""
    province =""

for line in urllib.request.urlopen("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"):
    string = line.decode("utf-8")
    f.write(string)                        #transforms the link to a txt for my convenience


for line in r:
    sum=0
    newcountry =country()
    tempname=[]
    tempprov=[]
    
    for x in range (4,len(line.split(','))): 
        sum=line.split(',')[x]

    tempname.append(line.split(',')[1])
    tempprov.append(line.split(',')[0])
    newcountry.name=tempname
    newcountry.province=tempprov
    newcountry.dailySick=sum
    
    
    Countries.append(newcountry)                 #this fills the whole list with countries and provinces 
   
    
def sickCount(y):                  #
    counter=0  
    
    for x in range (1,len(Countries)):
      if Countries[y].name == Countries[x].name:
          counter+=int(Countries[x].dailySick)
          
    return(counter)

def sickInOneCountry():     #Counts the sick in one country
    
  counter=0  
  CountryName = input("Please enter the name of the country :\n(First letter of each word must be Capitalized)\n")
  
  for x in range (0,len(Countries)):         #searches the list with the inputted name and ecery time it finds the name of the country it adds the sick to the sum
      if CountryName in Countries[x].name:
          print(Countries[x].province,Countries[x].name,Countries[x].dailySick)
          counter+=int(Countries[x].dailySick)
  print("The total sick in ",CountryName," are :",counter)

def Date_Subtraction( d2):         #this method subtracts two dates and takes the difference as a number
    d1="2020-1-22"
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def sickOfTheDay():  #Counts the sick of one day specific in all the countries
    date=input("Please enter the date  :\n(The format must be this Year-Month-Day numver only for example 2020-1-22)\n")
    day=Date_Subtraction(date)
    temp = open("dict.txt",mode = 'r',encoding = 'utf-8')  #due to the fact that the parser in r is at the of the file a need to open a new file 
    for line in temp:
        print("Country :",line.split(',')[1],"\tProvince:",line.split(',')[0],':',line.split(',')[day+4])       #prints the sick of the day that was entered +4 is beacuase the 4 first fields are used for other things in the txt
    temp.close()

def mostSick():     #counts the country with the biggest number of sick people 
    
    Max=0
    maxCountry=""
    num=0
    for y in range (1,len(Countries)):
        num=sickCount(y)
        
        if num >=Max :
            Max=num
            maxCountry=Countries[y].name
    print(maxCountry,Max)
os.system('cls')

print("What do you wish to see press the corresponding number 1/2/3.\n")          # simple menu with the user choices that call methods corresponting to the number entered.
choice =input("1)Press 1 to view the total sick of one country by name.\n2)Press 2 to choose one date to view the sick of all countries at that date.\n3)Press 3 to view the country with the most sick people.\n")
if int(choice) == 1:
    print("choice 1")
    os.system('cls')
    sickInOneCountry()
elif int(choice)  == 2:
    os.system('cls')
    sickOfTheDay()
elif int(choice)  == 3:
    os.system('cls')
    mostSick()        

f.close()  
r.close()