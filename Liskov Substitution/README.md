# Liskov Substitution

Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

In the non_ideal.py <br/>

The Square class is the sub-class of the Rectangle class, and relevant adjustments have to be made to abstract methods. For example, in the case of the Square class, setWidth() and setHeight() should set the side of the square.

In the ideal.py <br/>

The Square class directly inherits from the Shape class containing the get_area method.
Any child class of Shape has to give its implementation for the get_area method() only.
