import argparse
from confluent_kafka import Consumer, KafkaError

def consume_messages(kafka_broker, topic):
    conf = {
        'bootstrap.servers': kafka_broker,
        'group.id': 'python-consumer-group',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(conf)
    consumer.subscribe([topic])
    
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('Reached end of partition')
                elif msg.error():
                    print(f'Error: {msg.error()}')
            else:
                print(f'Received message: {msg.value().decode("utf-8")}')
    except KeyboardInterrupt:
        print("Consumer interrupted by user")
    finally:
        consumer.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kafka Consumer Script')
    parser.add_argument('--topic', required=True, help='Kafka topic')
    parser.add_argument('--kafka', required=True, help='Kafka broker address')
    args = parser.parse_args()
    
    consume_messages(args.kafka, args.topic)
