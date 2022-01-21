a=int(input("Enter an integer: "))
b=float(input("Enter an float number: "))
c=input("Enter a character: ")
d=input("Enter a string: ")
e=input("Enter a boolean value: ")
lst=[a,b,c,d]
tup=(a,b,c,d)


def func1():
    print("Integer: ",a)
    print("Float: ",b)
    print("Character: ",c)
    print("String: ",d)
    print("Boolean: ",e)
    print("List: ",lst)
    print("Tuple: ",tup)

func1()
print("\n\nSecond Function\n") 


def func2():
    name=input("Enter your Name: ")
    age=int(input("Enter your Age: "))
    gender=input("Enter your Gender: ")
    mt=input("Enter your Mother Tongue: ")
    country=input("Enter your country: ")
    aim=input("What is your aim in life: ")
    a=[name,age,gender,mt,aim, country]
    print('\n')
    print(f"Name:{a[0]} \nAge:{a[1]} \nGender:{a[2]} \nMother Tongue:{a[3]} \nCountry:{a[5]}\nAim: {a[4]}")

func2()

print("\nThird function\n\n")

def func3():
    n1=int(input("Enter number 1: "))
    n2=int(input("Enter number 2: "))
    lst=[n1,n2]
    print("These 2 numbers are represented in list as",lst)

func3()
