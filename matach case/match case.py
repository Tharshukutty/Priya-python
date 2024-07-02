# match case 

# week of days

n=int(input("enter a week days:"))

match n:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("pls enter 1 to 7 ")


# weekend or week days

a=input("enter a week days:")

match a:
    case "monday"| "tuesday"| "wednesday"| "thursday"| "friday":
        print("week days")
    case "saturday"| "sunday":
        print("weekend")
    case _:
        print("pls enter a week days")


# number of days in  month

y=input("enter a month:")

match y:
    case "January" | "March" | "May" | "July" | "August" | "October" | "December":
        print("number of days is 31")
    case "April" | "June" | "September" | "November":
        print("number ofdays is 30")
    case "feburary":
        if y%4==0 and y%400==0:
            print("number of days is 29")
        else:
            print("number of days is 28")
    case _:
        print("invalid month")


# number is zero, positive, negative

num=int(input("enter a number:"))

match num:
    case n if n>0:
        print("positive")
    case n if n<0:
        print("negative")
    case 0:
        print("zero")
    case _:
        print("invalid result")


# age in life stage

n=int(input("enter a number:"))

match n:
    case n if 0<=n<=1:
        print("infant")
    case n if 2<=n<=12:
        print("child")
    case n if 13<=n<=19:
        print("teenager")
    case n if 20<=n<=60:
        print("adult")
    case n if n>=61:
        print("senior citizen")
    case _:
        print("invalid age")

# shapes based on the number of sides

sides=int(input("enter a number:"))

match sides:
    case 3:
        print("triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case 6:
        print("hexagon")
    case 7:
        print("heptagon")
    case 8:
        print("octagan")
    case 9:
        print("nonagon")
    case 10:
        print("decagon")
    case _:
        print("invalid shapes")

# leap year

x=int(input("enter a year:"))

match x:
    case x if x% 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        print("true")
    case _:
        print("false")


# season based on month

n=input("enter a month:")

match n:
    case "december"| "january"| "february":
        print("winter")
    case "march"|"april"| "may":
        print("spring")
    case "june"| "july"| "august":
        print("summer")
    case "september"| "october"| "november":
        print("rainy")
    case _:
        print("wrong input")
    
# character is vowels or consonant

x=input("enter a letter:")

match x:
    case "a"|"e"|"i"|"o"|"u":
        print("vowels")
    case "b"|"c"|"d"|"f"|"g"|"h"|"j"|"k"|"l"|"m"|"n"|"p"|"q"|"r"|"s"|"t"|"V"|"W"|"x"|"Y"|"Z":
        print("consonant")
    case _:
        print("pls enter a letters")

 
