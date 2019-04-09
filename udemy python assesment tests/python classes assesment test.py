#Fill in the class to get height and radious of a cylinder and calculate its volume and surface area

class Cylinder():
    pie=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return Cylinder.pie*(self.radius**2)*self.height
    
    def surface_area(self):
       return 2*Cylinder.pie*self.radius*(self.radius+self.height)


my_cylinder=Cylinder(2,3)
print(my_cylinder.pie)
print(my_cylinder.volume())
print(my_cylinder.surface_area())

print(' ')


