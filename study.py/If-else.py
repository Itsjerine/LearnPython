#--PosNag Num---
x = int(input("Type number :"))
if (x==0):
    print(f"{x} is zero")
elif (x>0):
    print(str(x)+ "is positive number")
else:
    print("{} is negative number".format(x)) #.format(data type)-->string

# --- Score and grade ---
x = int(input("your score : "))
if x<=100 and x>=0: #check condition
    if (x>=80):
        print("you got grade A")
    elif (x>=70):
        print("you got grade B")
    elif x>=60:
        print("you got grade C")
    elif x>50:
        print("you got grade D")
    else:
        print("Stupid boy got F!!")
else: print("ERROR") #when you input nag num

# ---calculate BMI--- weight g->kg / height cm->m
weight = 6500
height = 165
BMI = (weight/100)/((height/100)**2) #print(BMI) print text only
print("{0:.2f}".format(BMI))

#---calculate BMI--- input
weight = float(input("Input ur W : "))
height = float(input("Input ur H : "))

BMI = weight/((height/100)**2)
print("{0:.2f}" .format(BMI))

if BMI>=0:
    if BMI<18.50:
        print("Underweight")
    elif 18.50<=BMI<=22.99:
        print("Healthyweight")
    elif 23<=BMI<=24.99:
        print("Overweight I")
    elif 25<=BMI<=29.99:
        print("Overweight II")
    else:
        print("Obesity")


import random #import library
num_random = random.randrange(1,10)
inp = int(input("Input Number : "))

if inp > num_random:
    print("My num is greater than random number")
elif inp < num_random:
    print("My num is less than random number")
else:
    print("WOW Exactly right!!")

print("-------------------------------")
print(f"random number is {num_random}")