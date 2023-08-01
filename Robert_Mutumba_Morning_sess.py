#matching and searching in python
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

def check(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email1 = "example@example.com"
email2 = "invalid_email"
email3 = "john.doe@example"

print(check(email1))  # True
print(check(email2))  # False
print(check(email3))  # False

#Generatores and Iterators
def factorial(ne):
    if ne==0:
        return 1
    else:
        return ne * factorial(ne-1)
for xe in range(1,10):
    print(factorial(xe))

def squares():
    for i in range(1,10):
      yield i**2

squares_iterator=squares()

for i in range(5):
    print(next(squares_iterator))

def factorial(num):
    if num==0:
            yield 1
    else:
            yield num * next(factorial(num-1))
for live in range(1,10):
    print(next(factorial(live)))

"""
#decorator
def decorator(func):
        def wrapper():
            print("Before")
            func()
            print("After")
        return wrapper
@my_decorator
def my_function():
     
"""

