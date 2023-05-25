from abc import ABC, abstractmethod


class Consumer:
    def __init__(self, producer):
        self.producer = producer

    def consume_content(self):
        data = self.producer.produce_content()
        print("Display data:", data)


class Producer(ABC):
    @abstractmethod
    def produce_content(self):
        pass


class APIProducer:
    def produce_content(self):
        return "API producing content"


class OSProducer:
    def produce_content(self):
        return "OS producing content"


consumer1 = Consumer(APIProducer())
consumer2 = Consumer(OSProducer())

consumer1.consume_content()
consumer2.consume_content()
