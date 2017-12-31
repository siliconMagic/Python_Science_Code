from traits.api import HasTraits, Color, Int, Float, Range

class Circle(HasTraits):
    color = Color
    
class Person(HasTraits):
    age = Int(30)
    weight = Float(22.5)
    
coefficient = Range(-1.0, 1.0, 0.0)

class Quadratic(HasTraits):
    c0 = coefficient
    c1 = coefficient
    c2 = coefficient
    
if __name__ == "__main__":
    q = Quadratic()
    print(q.trait("c0").trait_type)
    '''
    p = Person()
    print("%d %f" %(p.age, p.weight))
    circle = Circle()
    circle.color = "red"
    print(circle.color)
    circle.configure_traits()
    '''