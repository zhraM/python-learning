#practice1
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r ** 2 * 3.14
class Rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
c1 = Circle(3)
r1 = Rectangle(4,3)
print(c1.area())
print(r1.area())

#practice2
class Media:
    def play(self):
        print("Media is playing")
class Song(Media):
    def play(self):
        print("Song is playing")
class Podcast(Media):
    def play(self):
        print("Podcast is playing")
class Audiobook(Media):
    def play(self):
        print("Audiobook is playing")
medias = [
    Song(),
    Podcast(),
    Audiobook()
]
for media in medias:
    media.play()
    
#practice3
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def final_price(self):
        print("The product has't be sent")
class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
    def final_price(self):
        return self.price
class PhysicalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
    def final_price(self):
        return self.price + 80
class ImportedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
    def final_price(self):
        return 20 / 100 * self.price + self.price

products = [
    DigitalProduct("pen",200),
    PhysicalProduct("pc",1000),
    ImportedProduct("car",1000000)
]
for product in products:
    print(product.final_price())