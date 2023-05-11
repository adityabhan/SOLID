# Open-Closed

The <strong>open-closed</strong> principle states that classes, modules, and functions should be open for extension but closed for modification.<br/>

It means you should be able to extend the functionality of an existing class, module, or function without modifying the existing code/implementation.

In the non_ideal.py <br/>

Shape class has a method called <i>get_area</i> which is responsible for calculating the area of a given shape.
With this implementation every time a new shape is added, the previous implementation i.e. (<i>get_area</i> method in Shape class) has to be modified. This violates the Open-Closed principle.

In ideal.py <br/>

Shape class is now an Abstract class with abstract method <i>get_area</i>. This means each subclass has to define its own implementation for <i>get_area</i> method, thereby maintaining the Open-Closed principle. 