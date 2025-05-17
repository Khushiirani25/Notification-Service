from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import redis.asyncio as redis

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Async Redis client (Upstash with SSL)
r = redis.Redis(
    host="master-turtle-21405.upstash.io",
    port=6379,
    password="AVOdAAIjcDE1MjlkNzVhZDdjMGQ0MmVjOThhZTgxYzcxZWVhNzJjZXAxMA",
    decode_responses=True,
    ssl=True
)

class Notification(BaseModel):
    user_id: str
    type: str
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/notifications")
async def send_notification(notification: Notification):
    key = "notification_queue"
    await r.rpush(key, notification.json())  # Queue to be picked up by worker
    return {"status": "queued", "user": notification.user_id, "type": notification.type}
