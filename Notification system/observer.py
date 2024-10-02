# observer.py
class User:
    def __init__(self, name, notification_preference):
        self.name = name
        self.notification_preference = notification_preference

    def update(self, notification, message):
        print(f"{self.name} received a notification")
        notification.send(message)
