class Complex:
    def __init__(self, real ,imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real, "i +", self.imag, "j")  

##dunder function user hot h add, sub, multi,div, add
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg  = self.imag + num2.imag
        return Complex(newReal, newImg) 
    
    ##subtraction
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg  = self.imag - num2.imag
        return Complex(newReal, newImg) 

num1 = Complex(2,3) 
num1.showNumber()   

num2 = Complex(5,6)
num2.showNumber()

num3 = num1 - num2  ##subtraction  ya addition
num3.showNumber()


##qestion
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (27/7) * self.radius * self.radius
    
    def perimeter(self):
        return 2 * (27/7) * self.radius
            

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())  


# question 2
class Employee:
    def __init__(self, designation, department, salary):
        self.designation = designation
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Designation:", self.designation)
        print("Department:", self.department)
        print("Salary:", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # calling parent constructor
        super().__init__("Engineer", "IT", "70000")

    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        # call parent class showDetails
        super().showDetails()


eng1 = Engineer("Shivani", 21)
eng1.showDetails()



##question 3
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price  

odr1 = Order("chips", 30)
odr2 = Order("tea", 20)

print(odr1 > odr2) ##true
print(odr1 < odr2) ##false
