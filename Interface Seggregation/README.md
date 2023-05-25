# Interface Segregation

Segregation means keeping things separated, and the Interface Segregation Principle is about having specific interfaces rather than having one generic interface.

In the non_ideal.py <br/>

The Animal is an abstract class with two abstract methods feed_type and pet. Any sub/child class has to implement these two methods.

In the framed example, although the feed_type makes sense for Dogs and Tigers, but not every animal can be a pet.
But we have to write an implementation for the pet method in Tiger class.

In the ideal.py <br/>

A Pet class (subclass of Animal) is added that has the pet method. In this scenario, any domestic animal like Dog can inherit from the Pet class and the Tiger class does not have to write any implementation for the pet method.
