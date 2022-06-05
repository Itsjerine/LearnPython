animals = ["Cat","Rabbit","Dog"]
for i in animals:
    print(i)
    
for i in range(1,5,1): #(start,stop(n+1),เพิ่มครั้งละ)
    print(i)

def number(n):
    for i in range(0,n*2,2):
        print(i)
    print("-----------------")

number(2)
number(3)
number(4)


def number2(n):
    for i in range(2,n*2,2):
        print(i)
    print("-------------")

number2(2)
number2(3)
number2(4) #n*2 = 4*2 => 8 output!=8 ถึงแค่ 6
