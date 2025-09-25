#!/usr/bin/python3

class Employee:
    amnt = 1.04
    def __init__(self, name, email, pay):
        self.__name = name
        self.__email = email
        self.__pay = pay
        
    
    def calc_tax(self, rate):
       inc =  self.calc_salary(100)
       return inc - rate
    
    
    def calc_salary(self, value):
        return self.__pay + value
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.__name, self.__email, self.__pay)
    
    @classmethod
    def raise_amnt(cls, amount):
        # we can call class method through instance
        cls.amnt = amount 
    
    @classmethod
    def from_string(cls, emp_str):
        """alt to constructor"""
        first, email, pay = emp_str.split('-')
        return cls(first, email, pay)# generic for any class
    
    def __len__(self):
        return len(self.__name)
    
    def __str__(self):
        return "A {} name is {} and his email {}".format(type(self).__name__, self.__name, self.__email)


class Developer(Employee):
     def __str__(self):
         return super().__str__() + " and it is developer"
     
     
     def sumAll (self, *args):
         """for accepting dynamic no of args"""
         for item in args:
             print(item)
            
  

emp1 = Employee("ahmed","ahmed@yahoo", 1000)
print(emp1.calc_tax(5))

#print(Employee.__dict__)# show fn and class att
emp2 = Employee("moh","###yahoo", 300)
emp2.nickname = "Moo" ## this att added only for emp2
#print(emp1.__dict__) # show only instance att
# if we have class att, then modify it through obj like emp1.raise_amount
# it will be changed in emp1 only and appears in __dict__


# alt. constructors using class method

#classic method
emp_str_1 = 'John-Doe@mana-6000'
emp_str_2 = 'sara-sarr@mana-6000'
first, email, pay = emp_str_1.split('-')
Emp1 = Employee(first, email, pay)

#second method define class method
Emp2 = Employee.from_string(emp_str_2)
#print(help(Developer))

print(emp1)# using repr or print(emp1.__repr__()) same for __str__

print(int.__add__(1, 2))# instead of modify in __add__ itself
print(str.__add__('a', 'b'))
print('test'.__len__()) #len('test')
print(len(emp1))

Dev = Developer("Ahmed","@@", 1000)
print(Dev)