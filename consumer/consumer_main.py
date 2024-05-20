from kafka_consumer import KafkaMessageConsumer
from processor import process_in_logfile
from config import settings


def main():
    consumer = KafkaMessageConsumer(
        boostrap_servers=settings.BOOSTRAP_SERVERS,
        topic=settings.TOPIC,
        group_id=settings.GROUP_ID
    )
    consumer.consume_message(
        processor=lambda x: process_in_logfile(message=x)
        )
    
if __name__=="__main__":
    main()
