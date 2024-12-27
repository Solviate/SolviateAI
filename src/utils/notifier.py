
class Notifier:
    def __init__(self, service_name="Notification Service"):
        self.service_name = service_name

    def send(self, user, message):
        # Simulate sending a notification
        print(f"[{self.service_name}] Sending notification to {user}: {message}")

    def batch_notify(self, users, message):
        for user in users:
            self.send(user, message)
    