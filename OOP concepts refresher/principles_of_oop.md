### Principles of OOP 
1. Inheritance
    Inheritance is the process by which one class takes 
    on the attributes  and methods of another. Newely 
    formed classes are called child classes, and the classes
    that child classes are derived from are called parent classes

    child classes inherit all of the parent's attributes and methods 
    but can also extend and overrites attributes and methods that 
    are unique to themselves 

2. Polymorphism
    "Many shapes"
    we can write a code that works on the superclass, and it will work
    with any subclass type as well.

    Gives a way to use a class exactly like its parent, but each child 
    class keeps its own methods as they are 


3. Encapsulation
    Encapsulation is the mechanism of hiding of data implementation.

    Instance variables are kept private and accessor methods 
    are made public to achieve this. With this, we restrict access to 
    public methods (getter/setter)

    Instance methods can also kept private 

4. Abstraction 
    Abstraction can be thought of as a natural extension of Encapsulation.
    Applying Abstraction means that each object should only expose a high level
    mechanism for using it
    
    This mechanism should hide internal implementation details.
    It should only reveal operations relevant for the other objects.
    
oop_1.py 
1. Create  a class (blueprint)
2. Create a instance (object)
3. Class vs instance 
4. instance attributes: defined in __init__(self) --> init function
5. class attribute

oop_2.py
1. Instance method(sef)
2. Our methods can take Arguments and can return values 
3. Special "dunder" method(__str__ and __eq__)
4. @static methods

oop_3.py
1. Inheritance: ChildClass(BaseClass)
2. inherit, extend, override 
3. super(): __init__()
4. Polymorphism

oop_4.py
1. Encapsulation
2. Abstraction
3. public, private 
    Note : 
    _x is called a "protected" attribute (one underscore)
    __x is called a "private" attribute (double underscore)

    Here we have used the word "private" for internal attributes with only
    one leading underscore as well 
4. _foo(), _x
5. getter / setter 
6. getter -> @property 
7. setter --> @name