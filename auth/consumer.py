import json, os, django
from confluent_kafka import Producer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# from core.models import User . this part login con confluent kafka
consumer = Consumer({
    'bootstrap.servers': os.environ.get('KAFKA_BOOTSTRAP_SERVERS'),
    'security.protocol': os.environ.get('KAFKA_SECURITY_PROTOCOL'),
    'sasl.username': os.environ.get('KAFKA_USERNAME'),
    'sasl.password': os.environ.get('KAFKA_PASSWORD'),
    'sasl.mechanisms': 'PLAIN',
    'group.id': os.environ.get('KAFKA_GROUP_ID'),
    'auto.offset.reset': 'earliest',
})

consumer.subscribe([os.environ.get('KAFKA_TOPIC')])