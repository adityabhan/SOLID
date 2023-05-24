# Interface Seggregation

Segregation means keeping things separated, and the Interface Segregation Principle is about having specific interfaces rather than having one generic interface.

In the non_ideal.py <br/>

Animal is an abstract class with two absract methods feed_type and pet. Any sub/child class has to implement these two methods.

In the framed example, although the feed_type make sense for Dog and Tiger, but not every animal can be a pet.
So we have to write an implementation for pet method in Tiger class.

In the ideal.py <br/>

A Pet class (sub class of Animal) is added that has the pet method. In this scenario any domestic animal like Dog can inherit from the Pet class and Tiger class does not have to write implementation for the pet method.
