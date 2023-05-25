class Consumer:
    def __init__(self, api_producer):
        self.api_producer = api_producer

    def consume_content(self):
        data = self.api_producer.produce_content()
        print("Consuming content :", data)


class APIProducer:
    def produce_content(self):
        return "API producing content"


consumer = Consumer(APIProducer())
consumer.consume_content()
