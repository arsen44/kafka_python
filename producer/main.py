import argparse
from confluent_kafka import Producer

def produce_message(kafka_broker, topic, message):
    conf = {'bootstrap.servers': kafka_broker}
    producer = Producer(conf)
    
    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
    
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kafka Producer Script')
    parser.add_argument('--message', required=True, help='Message to produce')
    parser.add_argument('--topic', required=True, help='Kafka topic')
    parser.add_argument('--kafka', required=True, help='Kafka broker address')
    args = parser.parse_args()
    
    produce_message(args.kafka, args.topic, args.message)
