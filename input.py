#name = int(input("Hello My name is: "))
#city = int(input("I am from: "))
width =int(input("Enter width"))
height = int(input("Enter height"))
length =int(input("Enter length"))
radius =int(input("Enter radius"))
p = 22/7
areaRectangle = width*height
volumeRectangle =width*height*length

areaCircle = p*radius*radius
volumeCylinder = p*radius*radius*height

print ("Area of a rectangle =" ,areaRectangle)
print ("Volume of a rectangle =" ,volumeCylinder)
print ("Area of a circle =" ,areaCircle)
print ("Volume of a cylinder =" ,volumeCylinder)