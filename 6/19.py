"""Income tax is calculated as per the following table
Annual Income
Tax percentage
Up to 2.5 Lakhs
No Tax
Above 2.5 Lakhs to 5 Lakhs
5%
Above 5 Lakhs to 10 Lakhs
20%
Above 10 Lakhs to 50 Lakhs
30%

Write a program to find out the income tax amount of a person.
Program should accept annual income of a person
Output the amount of tax he has to pay
"""
ai=int(input("The annual income : "))
if ai<250000:
    print("you don't have to pay any tax")
elif 250000 < ai < 500000:
    ta=ai*0.05
    print("The amount of tax you have to pay is :"+str(ta))
elif 500000 < ai < 1000000:
    ta=ai*0.20
    print("The amount of tax you have to pay is :"+str(ta))
elif 1000000 < ai < 5000000:
    ta=ai*0.30
    print("The amount of tax you have to pay is :"+str(ta))
else:
    print("not defined")
