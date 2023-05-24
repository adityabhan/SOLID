# Liskov Substitution

Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

In the non_ideal.py <br/>

Square class is the sub class of Rectangle class, and relevant adjustments have to be made to abstract methods. For example in case of Square class setWidth should set the side of square.

In the ideal.py <br/>

Square class directly inherits from Shape class containing get_area method.
Any child class of Shape has to give its implementation for get_area method only.
