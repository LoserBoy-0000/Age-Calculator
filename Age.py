

from calendar import month
import datetime
today = str(datetime.date.today())
today1 = today.split('-')
Now_day = int(today1[2])
Now_month = int(today1[1])
Now_year = int(today1[0])
a = input("Enter your Date Of Birth (DD-MM-YY): ")
dob = a.split('-')

dob_day = int(dob[0])
dob_month = int(dob[1])
dob_year = int(dob[2])
if (dob_day<=31) and (dob_day > 0) and (dob_month<=12) and (dob_month>0) and (dob_year>1900):
    if dob_year==Now_year:
        if(dob_month<=Now_month):
            if(dob_month==Now_month):
                if(dob_day<=Now_day):
                    if(dob_day==Now_day):
                        print("You're the Youngest Hijo de puta that i have ever seen")
                    else:
                        d= Now_day-dob_day
                        print(f'your age is only {d} days mf ')
                else:
                     print("My program is right mf ")
            elif(dob_month<Now_month):
                m=Now_month-dob_month
                if m==1:
                    if dob_day>Now_day:
                        d=(30-dob_day)+Now_day
                        print(f'Your age is only 1 month and {d} days mf')
                    elif dob_day<Now_day:
                        d=(Now_day-dob_day)    
                        print(f'Your age is only 1 month and {d} days mf')
                    elif dob_day==Now_day:
                        print(f'Your age is only 1 month mf')
                else:    
                    if dob_day>Now_day:
                        d=(30-dob_day)+Now_day
                        print(f'Your age is only {m} months and {d} days mf')
                    elif dob_day<Now_day:
                        d=(Now_day-dob_day)    
                        print(f'Your age is only {m} months and {d} days mf')
                    elif dob_day==Now_day:
                        print(f'Your age is only {m} month mf')
        else:
            print("My program is right mf ")
    elif (dob_year<Now_year):
        y= Now_year-dob_year
        if(dob_day<Now_day):
            d=Now_day-dob_day
            if(Now_month>dob_month):
                m= Now_month-dob_month
                print(f'Your Age is {y} years,{m} months and {d} days ')
            elif (Now_month==dob_month) :
                print(f'Your Age is {y} years and {d} days')
            elif(Now_month<dob_month) :
                y=y-1
                m= (12-dob_month)+Now_month
                print(f'Your Age is {y} years,{m} months and {d} days ') 
        elif(dob_day == Now_day) :
            if(Now_month>dob_month):
                m = Now_month-dob_month
                print(f'Your Age is {y} years,{m} months ')
            elif (Now_month==dob_month) :
                print(f'Your Age is {y} years')
            elif(Now_month<dob_month) :
                y=y-1
                m= (12-dob_month)+Now_month
                print(f'Your Age is {y} years,{m} months') 
        elif (dob_day>Now_day):
            d = (30-dob_day)+Now_day
            if(dob_month==12):
                dob_month=0
                y = y-1
                m = Now_month-dob_month
                print(f'Your Age is {y} years,{m} months and {d} days ')
            else:
                dob_month = dob_month+1
                if(Now_month>dob_month):
                    m = Now_month-dob_month
                    print(f'Your Age is {y} years,{m} months and {d} days ')
                elif (Now_month==dob_month) :
                    print(f'Your Age is {y} years and {d} days')
                elif(Now_month<dob_month) :
                    y=y-1
                    m= (12-dob_month)+Now_month
                    print(f'Your Age is {y} years,{m} months and {d} days ')        
    else:
        print("Hijo de Puta")
else:
        print("Hijo de Puta abuelo")
a= input("Enter Any Key To Continue : ")
if a!= 2:
    exit()


