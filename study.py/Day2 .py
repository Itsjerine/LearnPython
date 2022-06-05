
def sum(num1,num2):
    print(num1+num2)
sum(34,35)


def number3(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j, end="") # After finishing that function not to do anything further
        print()
    print("-------------")

number3(2)
number3(3)
number3(4)


def show(n):
    ans = '' #str
    for i in range(1,n+1): # i = 1
        for j in range(1,n+1):
            ans += str(i*j) # ans=something + str i*j
        ans += "\n"
    print(ans,end="")
    # print(ans) #default of print has \n always
    print("----------")
show(2)
show(3)
show(4)

