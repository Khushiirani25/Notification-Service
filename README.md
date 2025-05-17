# 🚀 Notification Service with FastAPI nd Redis Cloud

This project implements a simple notification service using FastAPI and Redis. Users can send notifications of different types (Email, SMS, In-App) through a web form, which are then enqueued in a Redis queue. A background worker processes these notifications (placeholder for real logic such as sending emails or SMS).

---

## 📌 Features

- ✅ Send notifications to users via API
- ✅ View user-specific notifications
- ✅ HTML interface to send notifications
- ✅ Uses Redis Cloud (no local Redis install required)

---

## 🧾 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- redis-py

## ⚙️ Setup Instructions

1. **Clone the repository** (if applicable).

2. **Configure Redis:**  
   - This project uses [Upstash Redis Cloud](https://upstash.com) by default.  
   - Update Redis connection details (`host`, `port`, `password`) in the following files:  
     - `main.py`  
     - `redis_client.py`  
     - `worker.py`  
   - Alternatively, you can run your own Redis server and update credentials accordingly.

3. **Install dependencies:**

```bash
pip install fastapi uvicorn redis jinja2


## 🧩 How it works
    - When you submit the form on the web UI, a POST request is sent to /notifications.
    - The notification is stored in a Redis list (acting as a queue).
    - The worker script uses Redis' blocking pop (BLPOP) to fetch new notifications.
    - The worker processes notifications (currently, just prints to console; replace with real sending logic).

## ⚠️ Assumptions
    - Redis Cloud (Upstash) with SSL is used for secure Redis connections.
    - The notification processing logic is a placeholder and should be extended for real-world use (sending emails, SMS, etc.).
    - No authentication or user management implemented.
    - Simple UI with JavaScript and basic CSS styling.