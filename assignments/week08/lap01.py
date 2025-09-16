"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def getArea(self):
        area = self.__length * self.__width
        return f"Area =  {area}"

    def getPerimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        print("Perimeter = " + perimeter)  ##ไม่จำเป็นต้อง return เลยเปลี่ยนเป็น print

    def isSquare(self):
        if self.__length == self.__width:
            return f"True"
        else:
            return f"False"
        
rectangle = Rectangle(10,5)
print(rectangle.getArea())
rectangle.getPerimeter()
print(rectangle.isSqare())