class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

  #polymorphisms
  class shape:
    def area(self):
     pass

  class rectangle(shape):
    def __init__(self,length,width):
     self.length = length
     self.width = width
    def area(self):
     return self.length * self.width
     
  class circle(shape):
    def __init__(self,radius):
         self.radius = radius
    def area(self):
     return 3.14 * self.radius **2
    
    def circumstances(self):
      return 2*3.14*self.radius
    
    #create shape objects
  rec=rectangle(10,20)
  cir=circle(10)

    #calculate area
  print("The area ",rec.area())
  print("The aarea of the circle ",cir.area())

  from abc import ABC, abstractclassmethod

  class Animal(ABC):
     