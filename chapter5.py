# 1. Write a program using nested if to check whether a number is positive,
# negative, or zero, and if positive, also check whether it is even or odd.

n=int(input("enter a number"))
if n==0:
    print("number is zero")
elif n>0:
    print("number is positive")
    if n%2==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is negative")



# 2. Write a program using nested if to find the greatest among three numbers.

a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
c=int(input("enter third number:-"))
if a>b and a>c:
    print("a gretest number ")
elif b>a and b>c:
    print("b is gretest number")
else:
    print("c is gratest number")





# 3. Write a program using nested if to check whether a student has passed or
# failed, and if passed, assign a grade based on marks.



marks= int(input("enter your marks"))
if marks>=90  :
    print("grade a")
elif marks>=80:
    print("grade b")
elif marks>=70:
    print("grade c")
elif marks>=60:
    print("grade d")
else:
    print("fail")









# 4. Write a program using nested if to check whether a person is eligible to
# vote, and if eligible, check whether they are a first-time voter.



age=int(input("enter your age"))
is_first=True
if age>=18:
    if is_first:
        print("yes, he is eligible for vote and he is first  time voter")
    else:
        print("yes,eligible for vote but he is not first time")
else:
    print("not eligible")








    # 5. Write a program using nested if to check whether a number is divisible by
    #   5, and if yes, check whether it is also divisible by 10.


n=int(input("enter a number"))
if n%10==0:
    print("divisible by 10")
elif n%5==0:
    print(" disible by 5")
else:
    print("not disible")

# -----------and----------------------------------------



n=int(input("enter number:-"))
if n%10==0:
    print("disible by 5 and 10")
elif n%5==0:
    print("disible by 5")
else:
    print("not valid")








# 6. Write a program using nested if to check whether a character is an
# alphabet, and if it is an alphabet, check whether it is a vowel or consonant.


consonant="bcdfghjklmnopqrstvwxyz"
vowel="aeiou"
alphabet=input("enter a alphabet :-")
if alphabet in vowel:
    print("vowel")
elif alphabet in consonant:
    print("consonant")
else:
    print("invalid character")










# 7. Write a program using nested if to check whether a person is eligible for a
# job based on age, and if eligible, check whether they have the required
# qualification.


age = int(input("Enter your age: "))
qualification = input("Enter your qualification: ")

if age >= 21 and qualification == "graduate":
    print("Eligible for job")
elif age >= 21 and qualification != "graduate":
    print("Age eligible but qualification not matched")
else:
    print("Not eligible for job")








# 8. Write a program using nested if to check whether a number is greater than
# 50, and if yes, check whether it is also greater than 100.



n=int(input('enter a number'))
if n>=100:
    print("number is grater than 100")
elif n>=50:
    print("numnber is grater than 50")
else:
    print("number is small")






# Write a program using if-elif-else to check whether a number is positive,
# negative, or zero.


n=int(input("enter a number"))
if n==0:
    print("number is zero")
elif n>0:
    print("number is positive")
else:
    print("number is negative")









# 10. Write a program using elif to assign grades based on marks:
# A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).

percentage=float(input("enter percentage"))
if percentage>=90 and percentage<=100:
    print("A")
elif percentage>=80 and percentage<=89:
    print("b")
elif percentage>=70 and percentage<=79:
    print("c")
elif percentage>=60 and percentage<=69:
    print("d")
else:
    print("fail") 








# 11. Write a program using elif to check whether a given day number (1–7)
# corresponds to Monday–Sunday.


day=int(input("enter a day number"))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("not")






# 12. Write a program using elif to find the largest among three numbers.


a=int(input("enter a number:-"))
b=int(input("enter b number:-"))
c=int(input("enter c number:-"))
if a>b and a>c:
    print("a greater than")
elif b>a and b>c:
    print("b greter than")
else:
    print(" c greter than")






# 13. Write a program using elif to check whether a year is a leap year or not.,


year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")







# 14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or
# Senior.

age=int(input("enter age"))
if age<=10:
    print("child")
elif age<=20:
    print("teen")
elif age<=40:
    print("adult")
else:
    print("senior")








# 15. Write a program using elif to check whether a character is a vowel, consonant,
# digit, or special character.


alphabets="bcdfghjklmnpqrstvwxyz"
vowel="aeiou"
digit="1234567890"
special_character="@#$!"
ch=input("enter a character")
if ch in vowel:
    print("vowel")
elif ch in alphabets:
    print("consonant")
elif ch in digit:
    print("digit")
else:
    print("special charecter")







# 16. Write a program using elif to build a simple calculator for +, -, *, and /.

a=int(input("enter a"))
b=int(input("enter b"))
op = input("Enter operator (+, -, *, /): ")

if op=="+":
    print("sum:-",a+b)
elif op=="-":
    print("subtraction:-",a-b)
elif op=="*":
    print("multiplication:-",a*b)
elif op=="/":
    print("divisible:-",a/b)
else:
    print("not valid operator")







# 17. Write a program using elif to check whether a number is divisible by 2, 3, 5, or
# none of them.

n=int(input("enter number"))
if n%2==0 :
    print("numnber is divisible by 2")
elif n%3==0:
    print("number is divisible by 3")
elif n%5==0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 2,3,5") 









# 18. Write a program using elif to convert a numeric month value (1–12) into the month
# name.


month= int(input("enter number"))
if month==1:
    print("january")
elif month==2:
    print("febuary")
elif month==3:
    print("march")
elif month==4:
    print("april")
elif month==5:
    print("may")
elif month==6:
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("august")
elif month==9:
    print("september")
elif month==10:
    print("october")
elif month==11:
    print("november")
elif month==12:
    print("december")
else:
    print('none')









# 19. Write a program using elif to check the type of triangle: Equilateral, Isosceles, or
# Scalene.


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")



a=int(input("enter a side"))
b=int(input("enter b side"))
c=int(input("enter c "))
if a==b and b==c:
    print("equal tringle")
elif a==b or a==c or b==c:
    print("isosceles tringle")
else:
    print("scalene  tringle")









# 20. Write a program using elif to determine the season based on month number.



month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter Season")
elif month == 3 or month == 4 or month == 5:
    print("Summer Season")
elif month == 6 or month == 7 or month == 8:
    print("Rainy Season")
elif month == 9 or month == 10 or month == 11:
    print("Autumn Season")
else:
    print("Invalid month number")

#----------------------------------------------------------

winter_season="1212"
summer_season="345"
rainy_season="6789"
autumn_season="1011"
month = int(input("Enter month number (1-12): "))
if month in winter_season:
    print("winter season")
elif month in summer_season:
    print("summar season")
elif month in rainy_season:
    print("rainy season")
elif month in autumn_season:
    print("autumn season")
else:
    print("none")










# 21. Write a program using elif to calculate electricity bill based on unit ranges.

unit=int(input("enter electricity bill :-"))
if unit<=100:
    bill=unit*2
    print("electricity bill :-",bill)
elif unit<=200:
    bill=unit*3
    print(bill)
elif unit<=300:
    bill=unit*4
    print(bill)
else:
    print("not valid")












# 22. Write a program using elif to check whether a number is one-digit, two-digit,
# # three-digit, or more.

n=int(input("enetr number"))
if n<10:
    print("one number digit")
elif n<100:
    print("two number digit")
elif n<1000:
    print("three number digit")
else:
    print("more than digit")











# 23. Write a program using elif to check the result of a student: Distinction, First
# Class, Second Class, Pass, or Fail.

marks=int(input("enter marks"))
if marks>=95:
    print("d")
elif marks>=85:
    print("first ")
elif marks>=60:
    print("second")
elif marks>=40:
#     print("PASS")
# else:
#     print("fail")








 

# 24. Write a program using elif to convert percentage into grade category.


percentage=float(input("enter your percentage:-"))
if percentage>=90:
    print("grade A")
elif percentage>80:
    print("grade B")
elif percentage>70:
    print("grade C")
else:
    print("grade D(FAIL)")












# 25. Write a program using elif to check traffic light action based on color input.

color=input("enter color")
if color=="red":
    print("stop")
elif color=="yellow":
    print('ready')
else:
    print("go")








# 26. Write a program using elif to classify temperature as Cold, Moderate, or Hot.

temperature=int(input("enter tem"))
if temperature<=15:
    print("cold")
elif temperature<=30:
    print("moderate")
else:
    print("hot")




# . Write a program using elif to check the type of input number: zero, positive even,
# positive odd, or negative.

n=int(input("enter number"))
if n==0:
    print("number is zero")
elif n>0 and n%2==0:
    print("number is positive or even")
elif n>0 and n!=2==0:
    print("number is positive and odd")
else:
    print('negative')







    




  




 


















    