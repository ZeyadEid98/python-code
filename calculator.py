import math
class calc:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def Sum(self):
        print("Welcome In Add Function")
        print("Please Enter Your First Number: ")
        self.num1 = input()
        print("Please Enter Your Second Number: ")
        self.num2 = input()
        print("Answer: ",int(self.num1) + int(self.num2))

    def sub(self):
        print("Welcome In Sub Function")
        print("Please Enter Your First Number: ")
        self.num1 = input()
        print("Please Enter Your Second Number: ")
        self.num2 = input()
        print("Answer: ", int(self.num1) - int(self.num2))


    def mult(self):
        print("Welcome In multi Function")
        print("Please Enter Your First Number: ")
        self.num1 = input()
        print("Please Enter Your Second Number: ")
        self.num2 = input()
        print("Answer: ", int(self.num1) * int(self.num2))

    def div(self):
        print("Welcome In div Function")
        print("Please Enter Your First Number: ")
        self.num1 = input()
        print("Please Enter Your Second Number: ")
        self.num2 = input()
        print("Answer: ", int(self.num1) / int(self.num2))

    def mod(self):
        print("Welcome In mod Function")
        print("Please Enter Your First Number: ")
        self.num1 = input()
        print("Please Enter Your Second Number: ")
        self.num2 = input()
        print("Answer: ", int(self.num1) % int(self.num2))


    def pow(self):
        print("Welcome In Power Function")
        print("Please Enter Your Number: ")
        self.num1 = input()
        print("Please Enter Your Power: ")
        self.num2 = input()
        print("Answer: ", int(self.num1) ** int(self.num2))

    def sqrt(self):
        print("Welcome In Sqrt Function")
        print("Please Enter Your Number: ")
        self.num1 = input()
        print("Answer: ", math.sqrt(int(self.num1)))


obj = calc()

print("Welcome in this program")
print("To Continue click y: ")
cont = input("Enter y/n:    ")
while cont == "y":
    print("Select your operation: ")
    print("1- Add")
    print("2- Sub")
    print("3- Multi")
    print("4- Div")
    print("5- Mod")
    print("6- Pow")
    print("7- Sqrt")
    key = input("Enter Your Selection: ")
    if key == "1":
        obj.Sum()
    elif key == "2":
        obj.sub()
    elif key == "3":
        obj.mult()
    elif key == "4":
        obj.div()
    elif key == "5":
        obj.mod()
    elif key == "6":
        obj.pow()
    elif key == "7":
        obj.sqrt()
    else:
        break

print("Thank You for use this program  ^_^")
