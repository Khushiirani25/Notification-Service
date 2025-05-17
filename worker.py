import redis
import json
import time

# Redis connection
r = redis.Redis(
    host="master-turtle-21405.upstash.io",
    port=6379,
    password="AVOdAAIjcDE1MjlkNzVhZDdjMGQ0MmVjOThhZTgxYzcxZWVhNzJjZXAxMA",
    ssl=True
)

def process_notification(notification):
    print("📩 Processing:", notification)
    # Simulate action (e.g., sending email/SMS)
    time.sleep(1)

print("🔁 Worker started...")
while True:
    try:
        _, notification = r.blpop("notification_queue")
        data = json.loads(notification)
        process_notification(data)
    except Exception as e:
        print("⚠️ Error:", e)
        time.sleep(2)
