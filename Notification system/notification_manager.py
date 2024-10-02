# notification_manager.py
from notifications import NotificationFactory

class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
            cls._instance.observers = []
        return cls._instance

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, notification_type, message):
        notification = NotificationFactory.create_notification(notification_type)
        for observer in self.observers:
            if observer.notification_preference == notification_type:
                observer.update(notification, message)
