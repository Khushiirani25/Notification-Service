import redis
import json

# Redis Cloud credentials
REDIS_HOST = "master-turtle-21405.upstash.io"
REDIS_PORT = 6379
REDIS_PASSWORD = "AVOdAAIjcDE1MjlkNzVhZDdjMGQ0MmVjOThhZTgxYzcxZWVhNzJjZXAxMA"

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    ssl=True
)

def enqueue_notification(data):
    r.rpush("notification_queue", json.dumps(data))
