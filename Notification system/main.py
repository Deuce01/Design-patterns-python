from notification_manager import NotificationManager
from observer import User

# Create Notification Manager (Singleton)
manager = NotificationManager()

# Create Users (Observers)
alice = User("Alice", "email")
bob = User("Bob", "sms")
carol = User("Carol", "push")

# Add users to the Notification Manager
manager.add_observer(alice)
manager.add_observer(bob)
manager.add_observer(carol)

# Send notifications to users based on their preferences
manager.notify_observers("email", "You've got a new email!")
manager.notify_observers("sms", "You've got a new SMS!")
manager.notify_observers("push", "You've got a new push notification!")
