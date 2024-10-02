# 🛎️ **Notification Management System** 🛎️

Welcome to the **Notification Management System** project! 🎉 This system demonstrates the use of three common design patterns in Python: **Factory**, **Singleton**, and **Observer**.

---

## 📦 **Overview**
This project allows users (observers) to subscribe to various notification types (Email, SMS, Push) and receive updates when notifications are sent. It uses:
- **Factory Pattern**: To create different types of notifications.
- **Singleton Pattern**: To manage notification dispatching with a single instance.
- **Observer Pattern**: To notify users based on their subscription preferences.

---

## ⚙️ **Design Patterns Implemented**
1. **Factory Pattern**: Dynamically creates different types of notifications (Email, SMS, Push).
2. **Singleton Pattern**: Ensures only one instance of the **NotificationManager** exists.
3. **Observer Pattern**: Users subscribe to notification types and get updates when notifications are sent.

---

## 🗂️ **Project Structure**
```
notification_system/
│
├── notifications.py       # Factory and Notification classes
├── notification_manager.py # Singleton Notification Manager
├── observer.py            # User (Observer) classes
└── main.py                # Main entry point
```

---

## 🚀 **How to Run the Project**
1. **Clone the repository**:
   
2. **Run the main file**:
   ```bash
   python main.py
   ```

---

## 📋 **Example Usage**

- When running the system, users with different notification preferences (Email, SMS, Push) will be notified based on the type of notification sent.
- Sample output when sending notifications:

```
Alice received a notification
Sending Email: You've got a new email!
Bob received a notification
Sending SMS: You've got a new SMS!
Carol received a notification
Sending Push Notification: You've got a new push notification!
```

---

## 🔑 **Key Concepts**
- **Factory Pattern**: Easily extendable to new notification types (e.g., WhatsApp, Slack).
- **Singleton Pattern**: Centralized notification management with a single instance.
- **Observer Pattern**: User subscriptions and real-time notification dispatching.

---

## 🎯 **Future Improvements**
- Add more notification types (e.g., WhatsApp, Slack).
- Implement dynamic user subscriptions.
- Introduce priority notifications or batch processing.

---

Happy Coding! 💻
