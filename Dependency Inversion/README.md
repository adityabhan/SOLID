# Dependency Inversion

The Dependency Inversion principle states that classes or entities should depend upon abstractions instead of concrete implementations.

In the non_ideal.py <br/>

There is a Consumer class that consumes content produced by APIProducer. Here the implementation depends on the concrete class. In the future, if there is any change in produce_content, or if there is a new Producer, in such cases the concrete implementation is to change.

In the ideal.py <br/>

There is an abstract class Producer with abstract method produce_content. Every producer will inherit from this class and has to write its own implementation for the produce_content method.

Here the result of consume_content() will depend on the type of class/concrete implementation.
