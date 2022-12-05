date1=input("Enter date1 in format of dd/mm/year: ")# entering first date
x=date1[0]+date1[1]  #picking date from input
y=int(x)  #converting string of date(x) into int
z=date1[3]+date1[4] #picking month from date1
month1=int(z)  #converting string of month z into integer
k=date1[6:len(date1)]  #picking year from date1
year1=int(k)  #converting string of year (k) into integer


date2=input("Enter date2 in format of dd/mm/year: ")
a=date2[0]+date2[1]  #picking date from input of date2
b=int(a)         #converting string of date(x) into int
c=date2[3]+date2[4]  #picking month from date2
month2=int(c)      #converting string of month z into integer
d=date2[6:len(date2)]      #picking year from date2
year2=int(d)       #converting string of year (k) into integer
def leapyear(y,month1,b,month2,year1,year2):
    if (y in range(1,32) and month1 in range(1,13)) and (b in range(1,32) and month2 in range(1,13)):
        for i in range(year1,year2 +1):
            if  (i%400==0) or (i%4==0):
                print(i,end=",")
    print("\n")

def nonleapyear(y,month1,b,month2,year1,year2):
    if (y in range(1, 32) and month1 in range(1, 13)) and (b in range(1, 32) and month2 in range(1, 13)):
        for j in range(year1, year2+1):
            if (j % 4 != 0):
                print(j, end=",")
print("Leap-years: ")
leapyear(y,month1,b,month2,year1,year2)
print("Non-leapyears: ")
nonleapyear(y,month1,b,month2,year1,year2)




