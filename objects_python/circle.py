class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        
    @property
    def radius(self):
        return self.diameter / 2
    
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2
    
    
small = Circle(10)
print(small.diameter)
print(small.radius)
small.radius = 10
print(small.diameter)


# QUIZ
# Add a new property to the Rectangle class named area. It should calculate and return the area of the Rectangle instance (width * length).

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
        
#     @property
#     def area(self):
#         return self.width * self.length


# Let's add one more property to our Rectangle class. This time, add a perimeter property that returns the perimeter of the rectangle (length * 2 + width * 2).

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
        
#     @property
#     def area(self):
#         return self.width * self.length
    
#     @property
#     def perimeter(self):
#         return self.length * 2 +  self.width * 2



# QUIZ#2
# We need to be able to set the price of a product through a property setter.
# Add a new setter (@price.setter) method to the Product class that updates the _price attribute.

# class Product:
#     _price = 0.0
#     tax_rate = 0.12
  
#     def __init__(self, base_price):
#         self._price = base_price
    
#     @property
#     def price(self):
#         return self._price + (self._price * self.tax_rate)
    
    
#     @price.setter
#     def price(self, new_price):
#         self._price = new_price